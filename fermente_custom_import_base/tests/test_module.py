# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.modules.module import get_module_resource
from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged("post_install", "-at_install")
class TestModuleBase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ResPartner = cls.env["res.partner"]
        cls.Wizard = cls.env["base_import.import"]

    def _test_import_file(self, module, model, file_name, folder=False):
        preview_options = {"headers": True, "quoting": '"'}
        import_options = {"has_headers": True, "quoting": '"'}

        # Read File
        if not folder:
            folder = model
        file_path = get_module_resource(module, "tests/templates/", folder, file_name)
        extension = file_path.split(".")[-1]
        if extension == "csv":
            file_type = "text/csv"
        else:
            file_type = "Unimplemented Extension"

        file_content = open(file_path, "rb").read()

        # Create Wizard
        import_wizard = self.Wizard.create(
            {"res_model": model, "file": file_content, "file_type": file_type}
        )

        # Run Preview
        result_parse = import_wizard.parse_preview(preview_options)
        column_list = [x[0] for x in result_parse["preview"]]

        # Execute Import
        results = import_wizard.execute_import(column_list, column_list, import_options)

        items = self.env[model].browse(results.get("ids"))
        return items, results["messages"]

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
