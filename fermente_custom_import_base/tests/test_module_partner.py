# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from .test_module import TestModuleBase


@tagged("post_install", "-at_install")
class TestModulePartner(TestModuleBase):
    def test_01_import_supplier(self):
        partners, messages = self._test_import_file(
            "fermente_custom_import_base", "res.partner", "supplier.csv"
        )
        self.assertFalse(messages)
        self.assertEqual(len(partners), 1)
        self.assertEqual(partners.name, "Relais Vert")

    def test_02_existing_duplicates_name(self):
        partners, messages = self._test_import_file(
            "fermente_custom_import_base", "res.partner", "supplier.csv"
        )
        self.assertFalse(messages)
        partners, messages = self._test_import_file(
            "fermente_custom_import_base", "res.partner", "supplier.csv"
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].get("type"), "error")

    def test_03_import_supplier_new_duplicates_vat(self):
        partners, messages = self._test_import_file(
            "fermente_custom_import_base",
            "res.partner",
            "supplier_new_duplicates_vat.csv",
        )
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].get("type"), "error")
        self.assertEqual(messages[1].get("type"), "error")

    def test_04_import_supplier_existing_duplicates_vat(self):
        partners, messages = self._test_import_file(
            "fermente_custom_import_base",
            "res.partner",
            "supplier_existing_duplicates_vat.csv",
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].get("type"), "error")
