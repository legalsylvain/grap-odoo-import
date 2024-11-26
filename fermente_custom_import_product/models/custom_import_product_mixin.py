# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models
from odoo.exceptions import ValidationError


class CustomImportProductMixin(models.AbstractModel):
    _name = "custom.import.product.mixin"
    _description = "Abstract model to import product (variant and template)"
    _inherit = ["custom.import.mixin"]

    def _custom_import_prevent_duplicate_fields(self):
        res = super()._custom_import_prevent_duplicate_fields()
        res += ["name", "barcode"]
        return res

    def _custom_import_hook_vals(self, old_vals, new_vals):
        super()._custom_import_hook_vals(old_vals, new_vals)
        self._custom_import_handle_supplierinfo_vals(old_vals, new_vals)
        self._custom_import_handle_uom_po_vals(old_vals, new_vals)
        return

    def _custom_import_handle_supplierinfo_vals(self, old_vals, new_vals):
        supplier = self._custom_import_get_or_create(
            "res.partner", "name", old_vals, "grap_import_supplier_name"
        )
        if supplier:
            new_vals.update(
                {
                    "seller_ids": [
                        (
                            0,
                            False,
                            self._custom_import_prepare_supplierinfo_vals(
                                supplier, old_vals
                            ),
                        )
                    ],
                }
            )

    def _custom_import_handle_uom_po_vals(self, old_vals, new_vals):
        invoice_qty = old_vals.get("grap_import_supplier_invoice_qty") or 1
        if invoice_qty == 1:
            new_vals["uom_po_id"] = old_vals["uom_id"]
        else:
            uom = self.env["uom.uom"].browse(old_vals["uom_id"])
            purchase_uoms = uom.category_id.uom_ids.filtered(
                lambda x: x.factor_inv == invoice_qty
            )
            if not purchase_uoms:
                raise ValidationError(
                    _(
                        f"Uom Purchase not found. Base UoM {uom.name}."
                        f" Factor searched {invoice_qty}"
                    )
                )
            new_vals["uom_po_id"] = purchase_uoms[0].id

    def _custom_import_prepare_supplierinfo_vals(self, partner, vals):
        return {
            "partner_id": partner.id,
            "price": vals.get("grap_import_supplier_gross_price"),
            "product_code": vals.get("grap_import_supplier_product_code"),
            "product_name": vals.get("grap_import_supplier_product_name"),
            "min_qty": vals.get("grap_import_supplier_min_qty"),
        }
