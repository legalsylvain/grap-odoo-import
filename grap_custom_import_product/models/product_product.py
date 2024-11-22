# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = ["product.product", "custom.import.product.mixin"]

    @api.model
    def get_import_templates(self):
        return self.env["product.template"].get_import_templates()
