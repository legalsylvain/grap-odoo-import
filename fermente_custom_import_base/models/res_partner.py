# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import models

logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "custom.import.mixin"]

    def _custom_import_prevent_duplicate_fields(self):
        res = super()._custom_import_prevent_duplicate_fields()
        res += ["name", "vat"]
        return res
