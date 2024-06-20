# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from odoo.addons.grap_custom_import_product.tests.test_module import TestModuleProduct


@tagged("post_install", "-at_install")
class TestModuleProductSupplierinfoQtyMultiplier(TestModuleProduct):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ProductProduct = cls.env["product.product"]
        cls.classification_20 = cls.env.ref(
            "account_product_fiscal_classification.fiscal_classification_A_company_1"
        )

    def test_01_import_product_account_product_fiscal_classification(self):
        products, messages = self._test_import_file(
            "grap_custom_import_account_product_fiscal_classification",
            "product.product",
            "product.csv",
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 1)
        self.assertEqual(products.fiscal_classification_id, self.classification_20)
