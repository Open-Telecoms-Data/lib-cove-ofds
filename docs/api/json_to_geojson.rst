JSON to GeoJSON conversion API
==============================


Example
-------

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


Reference
---------



.. autoclass:: libcoveofds.geojson.JSONToGeoJSONConverter
  :members:
