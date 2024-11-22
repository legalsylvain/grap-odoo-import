# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from odoo.addons.fermente_custom_import_product.tests.test_module import (
    TestModuleProduct,
)


@tagged("post_install", "-at_install")
class TestModuleProductSupplierinfoQtyMultiplier(TestModuleProduct):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.classification_20 = cls.env.ref(
            "account_product_fiscal_classification.fiscal_classification_A_company_1"
        )

    def _test_import_product_account_product_fiscal_classification(self, model):
        products, messages = self._test_import_file(
            "fermente_custom_import_account_product_fiscal_classification",
            model,
            "product.csv",
            folder="product",
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 1)
        self.assertEqual(products.fiscal_classification_id, self.classification_20)

    def test_01_import_product_account_product_fiscal_classification_product(self):
        self._test_import_product_account_product_fiscal_classification(
            "product.product"
        )

    def test_02_import_product_account_product_fiscal_classification_template(self):
        self._test_import_product_account_product_fiscal_classification(
            "product.template"
        )
