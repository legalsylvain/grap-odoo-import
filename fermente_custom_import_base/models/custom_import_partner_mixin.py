# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class CustomImportPartnerMixin(models.AbstractModel):
    _name = "custom.import.partner.mixin"
    _description = "Abstract model to import partner (customer and supplier)"
    _inherit = ["custom.import.mixin"]

    def _custom_import_prevent_duplicate_fields(self):
        res = super()._custom_import_prevent_duplicate_fields()
        res += ["name", "vat"]
        return res
