# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class CustomImportProductMixin(models.AbstractModel):
    _name = "custom.import.product.mixin"
    _inherit = ["custom.import.product.mixin"]

    # pylint: disable=missing-return
    def _custom_import_hook_vals(self, old_vals, new_vals):
        super()._custom_import_hook_vals(old_vals, new_vals)
        self._custom_import_handle_product_label_vals(old_vals, new_vals)

    def _custom_import_handle_product_label_vals(self, old_vals, new_vals):
        label_ids = []
        for x in range(1, 4):
            field_name = f"grap_import_label_{x}"
            if old_vals.get(field_name, False):
                label_ids.append(old_vals[field_name])
        new_vals["label_ids"] = [(6, 0, label_ids)]
        # new_vals["label_ids"] = [Command.link(label_ids)]
