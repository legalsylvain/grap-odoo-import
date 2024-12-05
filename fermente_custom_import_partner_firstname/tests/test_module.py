# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from odoo.addons.fermente_custom_import_base.tests.test_module_partner import (
    TestModulePartner,
)


@tagged("post_install", "-at_install")
class TestModulePartnerFirstname(TestModulePartner):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_01_import_partner_first_name(self):
        partners, messages = self._test_import_file(
            "fermente_custom_import_partner_firstname",
            "res.partner",
            "partner.csv",
        )
        self.assertFalse(messages)
        self.assertEqual(len(partners), 4)

        partner_1 = partners.filtered(lambda x: x.email == "contact1@import.com")
        partner_2 = partners.filtered(lambda x: x.email == "contact2@import.com")
        partner_3 = partners.filtered(lambda x: x.email == "contact3@import.com")
        partner_4 = partners.filtered(lambda x: x.email == "contact4@import.com")

        self.assertEqual(partner_1.company_type, "person")
        self.assertEqual(partner_2.company_type, "person")
        self.assertEqual(partner_3.company_type, "person")
        self.assertEqual(partner_4.company_type, "company")

    def test_02_import_contact_individual_and_company(self):
        partners, messages = self._test_import_file(
            "fermente_custom_import_partner_firstname",
            "res.partner",
            "partner_incorrect.csv",
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].get("type"), "error")
