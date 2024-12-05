# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from odoo.addons.fermente_custom_import_product.tests.test_module import (
    TestModuleProduct,
)


@tagged("post_install", "-at_install")
class TestModulePurchaseDiscount(TestModuleProduct):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ProductProduct = cls.env["product.product"]
        cls.margin_33 = cls.env.ref(
            "product_margin_classification.classification_normal_margin"
        )
        cls.margin_50 = cls.env.ref(
            "product_margin_classification.classification_big_margin"
        )

    def _test_import_product_margin_classification(self, model):
        products, messages = self._test_import_file(
            "fermente_custom_import_product_margin_classification",
            model,
            "product.csv",
            folder="product",
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 4)

        product_1 = products.filtered(lambda x: x.name == "Product 1")
        self.assertEqual(product_1.margin_classification_id, self.margin_33)

        product_2 = products.filtered(lambda x: x.name == "Product 2")
        self.assertEqual(product_2.margin_classification_id, self.margin_50)

        product_3 = products.filtered(lambda x: x.name == "Product 3")
        product_4 = products.filtered(lambda x: x.name == "Product 4")
        self.assertEqual(
            product_3.margin_classification_id, product_4.margin_classification_id
        )

    def test_01_import_product_margin_classification_product(self):
        self._test_import_product_margin_classification("product.product")

    def test_02_import_product_margin_classification_template(self):
        self._test_import_product_margin_classification("product.template")
