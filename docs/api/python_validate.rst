Python Validate API
===================


Example
-------

.. code-block:: python

    from libcoveofds.schema import OFDSSchema
    from libcoveofds.python_validate import PythonValidate

    schema = OFDSSchema()
    worker = PythonValidate(schema)
    data = {
        "networks": [
            {"id": "1", "nodes": [
                {"id": "1"}
            ]}
        ]
    }
    out = worker.validate(data)
    print(out)

Reference
---------

.. autoclass:: libcoveofds.python_validate.PythonValidate
  :members:

For information on the schema object, see :doc:`schema`
