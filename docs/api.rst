Python API
==========

This page describes the Python API.

OFDSSchema
----------

Before instantiating the other classes on this page, you first need to create an ``OFDSSchema`` object:

.. autoclass:: libcoveofds.schema.OFDSSchema
  :members:

Example
~~~~~~~

.. code-block:: python

    from libcoveofds.schema import OFDSSchema

    schema = OFDSSchema()

JSONSchemaValidator
-------------------

.. autoclass:: libcoveofds.jsonschemavalidate.JSONSchemaValidator
  :members:

Returns:

.. autoclass:: libcoveofds.jsonschemavalidate.ValidationError
  :members:


For more information, see `handling validation errors <https://python-jsonschema.readthedocs.io/en/latest/errors/#handling-validation-errors>`__ in the jsonschema library documentation.

Example
~~~~~~~

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


PythonValidate
--------------

.. autoclass:: libcoveofds.python_validate.PythonValidate
  :members:

For more information on the checks and on the results format, see :doc:`checks`.

Example
~~~~~~~

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

AdditionalFields
----------------

.. autoclass:: libcoveofds.additionalfields.AdditionalFields
  :members:

For more information on the results format, see :doc:`additional_fields`.

Example
~~~~~~~

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

JSONToGeoJSONConverter
----------------------

.. autoclass:: libcoveofds.geojson.JSONToGeoJSONConverter
  :members:

For more information on the input and output formats, see the `JSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/json.html>`__ and the `GeoJSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/geojson.html>`__.

Example
~~~~~~~

.. code-block:: python

    from libcoveofds.geojson import JSONToGeoJSONConverter

    worker = JSONToGeoJSONConverter()
    data = {
            "networks": [
                {"id": "1", "nodes": [
                    {"id": "1"}
                ]}
            ]
        }
    worker.process_package(data)
    print(worker.get_nodes_geojson())
    print(worker.get_spans_geojson())
    print(worker.get_meta_json())

GeoJSONToJSONConverter
----------------------

.. autoclass:: libcoveofds.geojson.GeoJSONToJSONConverter
  :members:

For more information on the input and output formats, see the `GeoJSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/geojson.html>`__ and the `JSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/json.html>`__.

Example
~~~~~~~

.. code-block:: python

    from libcoveofds.geojson import GeoJSONToJSONConverter

    worker = GeoJSONToJSONConverter()
    nodes_data = {
        'type': 'FeatureCollection',
        'features': [
            {'type': 'Feature', 'geometry': None, 'properties': {'id': '1', 'network': {'id': '1'}}}
         ]
    }
    spans_data = {
        'type': 'FeatureCollection',
        'features': []
    }

    worker.process_data(nodes_data, spans_data)
    print(worker.get_json())
    print(worker.get_meta_json())
