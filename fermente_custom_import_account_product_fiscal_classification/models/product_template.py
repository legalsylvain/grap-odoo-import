# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    grap_import_vat_amount = fields.Float(string="VAT Amount (For import)", store=False)

    grap_import_list_price_vat_excl = fields.Float(
        string="Sale Price Vat Excl (For import)", store=False
    )

    grap_import_list_price_vat_incl = fields.Float(
        string="Sale Price Vat Incl (For import)", store=False
    )
