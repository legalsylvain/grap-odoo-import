# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Fermente - Demo Template for Custom Import",
    "summary": "Provide Demo Fermente template (xlsx file) to import" " data",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-import",
    "license": "AGPL-3",
    "depends": [
        # OCA
        "account_product_fiscal_classification",
        "l10n_fr_department_product_origin",
        "product_margin_classification",
        "product_net_weight",
        "product_origin",
        "product_supplierinfo_qty_multiplier",
        "purchase_discount",
        "purchase_triple_discount",
        # GRAP
        "product_label",
        "fermente_custom_import_base",
        "fermente_custom_import_product",
    ],
    "auto_install": False,
    "installable": True,
}
