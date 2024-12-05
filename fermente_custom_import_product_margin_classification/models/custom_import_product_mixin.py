# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.tools import float_compare


class CustomImportProductMixin(models.AbstractModel):
    _name = "custom.import.product.mixin"
    _inherit = ["custom.import.product.mixin"]

    def _custom_import_hook_vals(self, old_vals, new_vals):
        super()._custom_import_hook_vals(old_vals, new_vals)
        self._custom_import_handle_margin_classification_vals(old_vals, new_vals)
        return

    def _custom_import_handle_margin_classification_vals(self, old_vals, new_vals):
        profit_margin = (
            "grap_import_margin_rate" in old_vals
            and old_vals["grap_import_margin_rate"] * 100
        )
        if profit_margin:
            # Look for existing classification
            classifications = self.env["product.margin.classification"].search([])
            product_classification = False
            for classification in classifications:
                if not float_compare(
                    profit_margin,
                    classification.profit_margin,
                    precision_rounding=self.env["decimal.precision"].precision_get(
                        "Margin Rate"
                    ),
                ):
                    product_classification = classification
                    break

            if not product_classification:
                vals = {
                    "name": _(
                        "Margin Rate %(margin_rate)s %%", margin_rate=profit_margin
                    ),
                    "markup": 100 * (profit_margin / (100 - profit_margin)),
                }
                # If not found, create a new one
                product_classification = self.env[
                    "product.margin.classification"
                ].create(vals)

            new_vals["margin_classification_id"] = product_classification.id
