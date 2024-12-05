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
        cls.tax_20 = cls.env.ref(
            "account_product_fiscal_classification.account_tax_sale_20_company_1"
        )

    def _test_import_product_account_product_fiscal_classification(
        self, model, vat_included
    ):
        products, messages = self._test_import_file(
            "fermente_custom_import_account_product_fiscal_classification",
            model,
            "product.csv",
            folder="product",
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 2)

        product_1 = products.filtered(lambda x: x.name == "Product 1")
        self.assertEqual(product_1.fiscal_classification_id, self.classification_20)

        product_2 = products.filtered(lambda x: x.name == "Product 2")
        self.assertEqual(product_2.fiscal_classification_id, self.classification_20)

        if vat_included:
            self.assertEqual(product_1.list_price, 1.21)
            self.assertEqual(product_2.list_price, 1.20)
        else:
            self.assertEqual(product_1.list_price, 1.00)
            self.assertEqual(product_2.list_price, 0.99)

    def test_01_import_product_account_product_fiscal_classification_product_vat_excl(
        self,
    ):
        self.tax_20.price_include = False
        self._test_import_product_account_product_fiscal_classification(
            "product.product", False
        )

    def test_02_import_product_account_product_fiscal_classification_product_vat_incl(
        self,
    ):
        self.tax_20.price_include = True
        self._test_import_product_account_product_fiscal_classification(
            "product.product", True
        )

    def test_11_import_product_account_product_fiscal_classification_template_vat_excl(
        self,
    ):
        self.tax_20.price_include = False
        self._test_import_product_account_product_fiscal_classification(
            "product.template", False
        )

    def test_12_import_product_account_product_fiscal_classification_template_vat_incl(
        self,
    ):
        self.tax_20.price_include = True
        self._test_import_product_account_product_fiscal_classification(
            "product.template", True
        )
