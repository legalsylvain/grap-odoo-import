# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = "product.template"

    grap_import_vat_amount = fields.Float(string="VAT Amount (For import)", store=False)

    # pylint: disable=missing-return
    def _custom_import_hook_vals(self, old_vals, new_vals):
        super()._custom_import_hook_vals(old_vals, new_vals)
        self._custom_import_handle_fiscal_classification_id(old_vals, new_vals)

    def _custom_import_get_fiscal_classifications(self, vat_amount):
        domain = expression.OR(
            [[("company_id", "=", self.env.company.id)], [("company_id", "=", False)]]
        )
        if vat_amount:
            domain = expression.AND(
                [domain, [("sale_tax_ids.amount", "=", 100 * vat_amount)]]
            )
        else:
            domain = expression.AND([domain, [("sale_tax_ids", "=", False)]])

        return (
            self.env["account.product.fiscal.classification"]
            .search(domain)
            .filtered(lambda x: len(x.sale_tax_ids) < 2)
        )

    def _custom_import_handle_fiscal_classification_id(self, old_vals, new_vals):
        vat_amount = old_vals.get("grap_import_vat_amount")
        if not vat_amount and not self.env.context.get("install_mode"):
            raise ValidationError(
                _(
                    "No VAT Amount found for the product %(product_name)s",
                    product_name=old_vals.get("name"),
                )
            )
        classifications = self._custom_import_get_fiscal_classifications(vat_amount)

        if len(classifications) == 1:
            new_vals["fiscal_classification_id"] = classifications.id
            return

        elif len(classifications) == 0:
            raise ValidationError(
                _(
                    "No Fiscal Classification Found for the product %(product_name)s."
                    " Vat Amount %(vat_amount)s",
                    product_name=old_vals.get("name"),
                    vat_amount=vat_amount,
                )
            )

        raise ValidationError(
            _(
                "Many Fiscal Classifications Found for the product %(product_name)s."
                " Vat Amount %(vat_amount)s. Fiscal Classifications : %(classification_names)s",
                product_name=old_vals.get("name"),
                vat_amount=vat_amount,
                classification_names=",".join(classifications.mapped("name")),
            )
        )
