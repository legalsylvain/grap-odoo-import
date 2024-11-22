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

    def _test_import_purchase_discount(self, model):
        products, messages = self._test_import_file(
            "fermente_custom_import_purchase_discount",
            model,
            "product.csv",
            folder="product",
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 1)
        self.assertEqual(products.seller_ids.discount, 10.0)

    def test_01_import_purchase_discount_product(self):
        self._test_import_purchase_discount("product.product")

    def test_02_import_purchase_discount_template(self):
        self._test_import_purchase_discount("product.template")