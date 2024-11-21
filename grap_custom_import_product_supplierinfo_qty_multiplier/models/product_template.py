# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    grap_import_supplier_multiplier_qty = fields.Float(
        string="Product Package Quantity - Supplier (For import)", store=False
    )

    def _custom_import_prepare_supplierinfo_vals(self, partner, vals):
        res = super()._custom_import_prepare_supplierinfo_vals(partner, vals)
        res["multiplier_qty"] = vals.get("grap_import_supplier_multiplier_qty")
        return res
