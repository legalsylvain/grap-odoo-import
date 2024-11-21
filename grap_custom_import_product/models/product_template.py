# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ["product.template", "custom.import.product.mixin"]

    grap_import_supplier_name = fields.Char(
        string="Supplier Name (For import)", store=False
    )
    grap_import_supplier_product_code = fields.Char(
        string="Product Code - Supplier (For import)", store=False
    )
    grap_import_supplier_product_name = fields.Char(
        string="Product Name - Supplier (For import)", store=False
    )
    grap_import_supplier_min_qty = fields.Monetary(
        string="Product Min Quantity - Supplier (For import)", store=False
    )
    grap_import_supplier_gross_price = fields.Monetary(
        string="Product Gross Price - Supplier (For import)", store=False
    )
