# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    grap_import_supplier_discount_2 = fields.Float(
        string="Supplier Discount 2 (For import)", store=False
    )

    grap_import_supplier_discount_3 = fields.Float(
        string="Supplier Discount 3 (For import)", store=False
    )
