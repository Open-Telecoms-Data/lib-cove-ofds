JSON Schema Validate API
========================


Example
-------

.. code-block:: python

    from libcoveofds.schema import OFDSSchema
    from libcoveofds.jsonschemavalidate import JSONSchemaValidator

    schema = OFDSSchema()
    worker = JSONSchemaValidator(schema)
    data = {
        "networks": "many"
    }
    out = worker.validate(data)
    print([i.json() for i in out])


Reference
---------


.. autoclass:: libcoveofds.jsonschemavalidate.JSONSchemaValidator
  :members:

.. autoclass:: libcoveofds.jsonschemavalidate.ValidationError
  :members:


For information on the schema object, see :doc:`schema`
