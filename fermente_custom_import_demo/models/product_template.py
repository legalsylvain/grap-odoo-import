# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def get_import_templates(self):
        return [
            {
                "label": _("Import Template for Fermente CAE"),
                "template": "fermente_custom_import_product/static/xlsx/template_product.xlsx",
            }
        ]
