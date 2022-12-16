GeoJSON to JSON conversion API
==============================


Example
-------

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


Reference
---------

.. autoclass:: libcoveofds.geojson.GeoJSONToJSONConverter
  :members:

