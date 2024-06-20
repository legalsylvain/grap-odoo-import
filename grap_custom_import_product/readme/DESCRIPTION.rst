This module improve the "import" features provided by Odoo.

It provides generic tools for that purpose, and improve imports for some models.

* ``product.product``:

    * Prevent to create duplicates regarding ``name`` and ``barcode`` fields.

    * Allow to create main ``seller_ids``, based on supplier information fields.
