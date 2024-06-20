# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from odoo.addons.grap_custom_import_base.tests.test_module import TestModuleBase


@tagged("post_install", "-at_install")
class TestModuleProduct(TestModuleBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ProductProduct = cls.env["product.product"]

    def test_01_import_product(self):
        products, messages = self._test_import_file(
            "grap_custom_import_product", "product.product", "product.csv"
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 3)
        coca_cola = products.filtered(lambda x: x.name == "Coca Cola (Import)")
        self.assertEqual(len(coca_cola), 1)
        self.assertEqual(coca_cola.standard_price, 3.33)
        self.assertEqual(coca_cola.mapped("seller_ids.partner_id.name"), ["Coke Corp"])
        self.assertEqual(coca_cola.mapped("seller_ids.product_code"), ["CC"])
        self.assertEqual(coca_cola.mapped("seller_ids.product_name"), ["BOTTLE 33CL"])
