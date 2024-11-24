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
        cls.label_organic = cls.env.ref("product_label.label_agriculture_biologique")
        cls.label_gluten_free = cls.env.ref("product_label.label_gluten_free")
        cls.label_max_havelaar = cls.env.ref("product_label.label_max_havelaar")

    def _test_import_product_label(self, model):
        products, messages = self._test_import_file(
            "fermente_custom_import_product_label",
            model,
            "product.csv",
            folder="product",
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 2)

        product_1 = products.filtered(lambda x: x.name == "Product 1")
        self.assertEqual(
            product_1.label_ids, self.label_organic | self.label_gluten_free
        )

        product_2 = products.filtered(lambda x: x.name == "Product 2")
        self.assertEqual(product_2.label_ids, self.label_max_havelaar)

    def test_01_import_product_label_product(self):
        self._test_import_product_label("product.product")

    def test_02_import_product_label_template(self):
        self._test_import_product_label("product.template")
