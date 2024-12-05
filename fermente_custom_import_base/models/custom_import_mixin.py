# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.exceptions import ValidationError


class CustomImportMixin(models.AbstractModel):
    _name = "custom.import.mixin"
    _description = "Mixin providing helper for imports"

    def _custom_import_prevent_duplicate_fields(self):
        """Define the fields that will be used to prevent
        Duplicates in the import"""
        return []

    def _custom_import_hook_vals(self, old_vals, new_vals):
        # Check if existing duplicates are present in the database
        for field in self._custom_import_prevent_duplicate_fields():
            if new_vals.get(field):
                items = self.search([(field, "=", new_vals.get(field))])
                if items:
                    raise ValidationError(
                        _(
                            "The following items still exist in the database"
                            " for the field %(field)s. Values: %(values)s",
                            field=field,
                            values=",".join(items.mapped(field)),
                        )
                    )
        return new_vals

    def _custom_import_hook_check(self, vals_list):
        self._custom_import_check_duplicates_new_vals(vals_list)

    def _custom_import_check_duplicates_new_vals(self, vals_list):
        for field in self._custom_import_prevent_duplicate_fields():
            duplicates = []
            for vals in vals_list:
                if vals.get(field):
                    if vals[field] in duplicates:
                        raise ValidationError(
                            _(
                                "The file contain many item(s) with"
                                " the same value '%(value)s' for the"
                                " field '%(field)s'.",
                                field=field,
                                value=vals[field],
                            )
                        )
                    duplicates.append(vals[field])

    def _custom_import_get_or_create(
        self, model_name, search_field_name, vals, field_name
    ):
        ItemModel = self.env[model_name]
        if not vals.get(field_name):
            return False
        items = ItemModel.search([(search_field_name, "=", vals[field_name])])
        if len(items) == 0:
            return ItemModel.create({"name": vals[field_name]})
        elif len(items) == 1:
            return items
        elif len(items) >= 2:
            raise ValidationError(
                _(
                    "%(item_qty)d items found for the field %(field_name)s."
                    " Value: '%(value)s'."
                ),
                item_qty=len(items),
                field_name=field_name,
                value=vals["field_name"],
            )

    # Overload Section
    def _load_records_create(self, vals_list):
        # This function is called in many places in odoo Core
        # to create records, specially when loading
        # 'demo' or 'data' from xml files.
        # We only want to alter data in a 'import' process.
        if not self.env.context.get("import_file"):
            return super()._load_records_create(vals_list)

        new_vals_list = []
        for vals in vals_list:
            new_vals = vals.copy()
            self._custom_import_hook_vals(vals, new_vals)
            new_vals_list.append(new_vals)

        self._custom_import_hook_check(new_vals_list)

        return super()._load_records_create(new_vals_list)
