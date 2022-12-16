Additional Fields API
=====================


Example
-------

.. code-block:: python

    from libcoveofds.schema import OFDSSchema
    from libcoveofds.additionalfields import AdditionalFields

    schema = OFDSSchema()
    worker = AdditionalFields(schema)
    data = {
        "networks": [
            {"id": "1", "cat": "socks"}
        ]
    }
    out = worker.process(data)
    print(out)


Reference
---------

.. autoclass:: libcoveofds.additionalfields.AdditionalFields
  :members:


For information on the schema object, see :doc:`schema`
