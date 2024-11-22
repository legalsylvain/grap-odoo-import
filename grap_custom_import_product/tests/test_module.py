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
        cls.unit_uom = cls.env.ref("uom.product_uom_unit")
        cls.unit_dozen = cls.env.ref("uom.product_uom_dozen")

    def _test_import_product(self, model):
        products, messages = self._test_import_file(
            "grap_custom_import_product", model, "product.csv", folder="product"
        )
        self.assertFalse(messages)
        self.assertEqual(len(products), 3)

        # Line Coca Cola
        coca_cola = products.filtered(lambda x: x.name == "Coca Cola (Import)")
        self.assertEqual(len(coca_cola), 1)
        self.assertEqual(coca_cola.standard_price, 3.35)
        self.assertEqual(coca_cola.uom_id, self.unit_uom)
        self.assertEqual(coca_cola.uom_po_id, self.unit_uom)

        supplierinfo = coca_cola.mapped("seller_ids")
        self.assertEqual(len(supplierinfo), 1)
        self.assertEqual(supplierinfo.partner_id.name, "Coke Corp")
        self.assertEqual(supplierinfo.product_code, "CC")
        self.assertEqual(supplierinfo.product_name, "BOTTLE 33CL")
        self.assertEqual(supplierinfo.price, 3.33)
        self.assertEqual(supplierinfo.min_qty, 6)

        # Line Product C
        product_c = products.filtered(lambda x: x.name == "Product C (Import)")
        self.assertEqual(len(product_c), 1)
        self.assertEqual(product_c.uom_id, self.unit_uom)
        self.assertEqual(product_c.uom_po_id, self.unit_dozen)

    def test_01_import_product_product(self):
        self._test_import_product("product.product")

    def test_02_import_product_template(self):
        self._test_import_product("product.template")
