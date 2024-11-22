# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class CustomImportProductMixin(models.AbstractModel):
    _name = "custom.import.product.mixin"
    _inherit = ["custom.import.product.mixin"]

    def _custom_import_prepare_supplierinfo_vals(self, partner, vals):
        res = super()._custom_import_prepare_supplierinfo_vals(partner, vals)
        res["discount2"] = (vals.get("grap_import_supplier_discount_2") or 0.0) * 100
        res["discount3"] = (vals.get("grap_import_supplier_discount_3") or 0.0) * 100
        return res
