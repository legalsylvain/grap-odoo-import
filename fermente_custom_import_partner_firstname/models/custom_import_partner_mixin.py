# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.exceptions import ValidationError


class CustomImportPartnerMixin(models.AbstractModel):
    _name = "custom.import.partner.mixin"
    _inherit = ["custom.import.partner.mixin"]

    def _custom_import_hook_vals(self, old_vals, new_vals):
        super()._custom_import_hook_vals(old_vals, new_vals)
        self._custom_import_handle_company_type(old_vals, new_vals)
        return

    def _custom_import_handle_company_type(self, old_vals, new_vals):
        if old_vals.get("name"):
            new_vals["company_type"] = "company"
        else:
            new_vals = "person"

    def _custom_import_hook_check(self, vals_list):
        super()._custom_import_hook_check(vals_list)
        for vals in vals_list:
            if (vals.get("firstname") or vals.get("lastname")) and vals.get("name"):
                raise ValidationError(
                    _(
                        "The file contains contacts that has first name or last name AND"
                        " name fields defined. Please set a name for a company"
                        " or a first name / last name for an individual."
                        " First Name: %(firstname)s ; "
                        " Last Name: %(lastname)s ; "
                        " Name: %(name)s",
                        name=vals.get("name"),
                        firstname=vals.get("firstname"),
                        lastname=vals.get("lastname"),
                    )
                )
        return
