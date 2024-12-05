# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    grap_import_label_1 = fields.Many2one(
        comodel_name="product.label", string="Label 1 (For import)", store=False
    )

    grap_import_label_2 = fields.Many2one(
        comodel_name="product.label", string="Label 2 (For import)", store=False
    )

    grap_import_label_3 = fields.Many2one(
        comodel_name="product.label", string="Label 3 (For import)", store=False
    )
