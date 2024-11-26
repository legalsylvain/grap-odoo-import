# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.exceptions import ValidationError
from odoo.osv import expression


class CustomImportProductMixin(models.AbstractModel):
    _name = "custom.import.product.mixin"
    _inherit = ["custom.import.product.mixin"]

    def _custom_import_hook_vals(self, old_vals, new_vals):
        super()._custom_import_hook_vals(old_vals, new_vals)
        self._custom_import_handle_fiscal_classification_id(old_vals, new_vals)
        return

    def _custom_import_fiscal_classification_domain(self, vat_amount):
        domain = expression.OR(
            [[("company_id", "=", self.env.company.id)], [("company_id", "=", False)]]
        )
        if vat_amount:
            domain = expression.AND(
                [domain, [("sale_tax_ids.amount", "=", 100 * vat_amount)]]
            )
        else:
            domain = expression.AND([domain, [("sale_tax_ids", "=", False)]])

        return domain

    def _custom_import_handle_fiscal_classification_id(self, old_vals, new_vals):
        vat_amount = old_vals.get("grap_import_vat_amount")
        if not vat_amount and not self.env.context.get("install_mode"):
            raise ValidationError(
                _(
                    "No VAT Amount found for the product %(product_name)s",
                    product_name=old_vals.get("name"),
                )
            )
        domain = self._custom_import_fiscal_classification_domain(vat_amount)

        classifications = (
            self.env["account.product.fiscal.classification"]
            .search(domain)
            .filtered(lambda x: len(x.sale_tax_ids) < 2)
        )

        if len(classifications) == 1:
            new_vals["fiscal_classification_id"] = classifications.id

        elif len(classifications) == 0:
            raise ValidationError(
                _(
                    "No Fiscal Classification Found for the product %(product_name)s."
                    " Vat Amount %(vat_amount)s",
                    product_name=old_vals.get("name"),
                    vat_amount=vat_amount,
                )
            )
        else:
            raise ValidationError(
                _(
                    "Many Fiscal Classifications Found for the product %(product_name)s."
                    " Vat Amount %(vat_amount)s."
                    " Fiscal Classifications : %(classification_names)s",
                    product_name=old_vals.get("name"),
                    vat_amount=vat_amount,
                    classification_names=",".join(classifications.mapped("name")),
                )
            )

        # If Specific Vat Excl / VAT Incl field are set, we use it, depending of the
        # the configuration of the fiscal classification
        if (
            all(classifications.mapped("sale_tax_ids.price_include"))
            and "grap_import_list_price_vat_incl" in old_vals
        ):
            new_vals["list_price"] = old_vals["grap_import_list_price_vat_incl"]
        elif "grap_import_list_price_vat_excl" in old_vals:
            new_vals["list_price"] = old_vals["grap_import_list_price_vat_excl"]
