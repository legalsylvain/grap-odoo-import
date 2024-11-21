# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = ["product.product", "custom.import.product.mixin"]

    # def _custom_import_prevent_duplicate_fields(self):
    #     res = super()._custom_import_prevent_duplicate_fields()
    #     res += ["name", "barcode"]
    #     return res

    # grap_import_supplier_name = fields.Char(
    #     string="Supplier Name (For import)", store=False
    # )
    # grap_import_supplier_product_code = fields.Char(
    #     string="Product Code - Supplier (For import)", store=False
    # )
    # grap_import_supplier_product_name = fields.Char(
    #     string="Product Name - Supplier (For import)", store=False
    # )
    # grap_import_supplier_min_qty = fields.Monetary(
    #     string="Product Min Quantity - Supplier (For import)", store=False
    # )
    # grap_import_supplier_gross_price = fields.Monetary(
    #     string="Product Gross Price - Supplier (For import)", store=False
    # )

    # # pylint: disable=missing-return
    # def _custom_import_hook_vals(self, old_vals, new_vals):
    #     super()._custom_import_hook_vals(old_vals, new_vals)
    #     self._custom_import_handle_supplierinfo_vals(old_vals, new_vals)

    # def _custom_import_handle_supplierinfo_vals(self, old_vals, new_vals):
    #     supplier = self._custom_import_get_or_create(
    #         "res.partner", "name", old_vals, "grap_import_supplier_name"
    #     )
    #     if supplier:
    #         new_vals.update(
    #             {
    #                 "seller_ids": [
    #                     (
    #                         0,
    #                         False,
    #                         self._custom_import_prepare_supplierinfo_vals(
    #                             supplier, old_vals
    #                         ),
    #                     )
    #                 ],
    #                 "standard_price": self._custom_import_prepare_standard_price(
    #                     old_vals
    #                 ),
    #             }
    #         )

    # def _custom_import_prepare_supplierinfo_vals(self, partner, vals):
    #     return {
    #         "partner_id": partner.id,
    #         "price": vals.get("grap_import_supplier_gross_price"),
    #         "product_code": vals.get("grap_import_supplier_product_code"),
    #         "product_name": vals.get("grap_import_supplier_product_name"),
    #         "min_qty": vals.get("grap_import_supplier_min_qty"),
    #     }

    # def _custom_import_prepare_standard_price(self, vals):
    #     return vals.get("grap_import_supplier_gross_price")
