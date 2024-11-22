# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class CustomImportCreateRecursiveMixin(models.AbstractModel):
    _name = "custom.import.create.recursive.mixin"
    _description = "Mixin providing recurring creation"
    " in the import process"

    @api.model
    def name_create(self, name):
        print("name_create::", self._name)
        return super().name_create(self, name)

    @api.model_create_multi
    def create(self, vals_list):
        print("create::", self._name)
        for vals in vals_list:
            pass
        res = super().create(vals_list)