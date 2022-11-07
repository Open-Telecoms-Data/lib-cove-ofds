#!/bin/bash

# This regenerates all expected test data from the current library
# After changing some big thing in code, you can run this
#
# Note you must then check the diff very carefully to make sure it's what you expect!!!
# This is not a easy way to just make your tests pass!
# The diff in the expected data should be reviewed very carefully in pull requests!
#

# Additional fields
libcoveofds  af  tests/fixtures/additionalfields/basic_1.input.json > tests/fixtures/additionalfields/basic_1.expected.json

# GeoJSON to JSON
libcoveofds gjtoj --outputmetafilename tests/fixtures/geojson_to_json/basic_1.meta.expected.json tests/fixtures/geojson_to_json/basic_1.nodes.geo.json tests/fixtures/geojson_to_json/basic_1.spans.geo.json  tests/fixtures/geojson_to_json/basic_1.expected.json
libcoveofds gjtoj --outputmetafilename tests/fixtures/geojson_to_json/no_geometry_1.meta.expected.json  tests/fixtures/geojson_to_json/no_geometry_1.nodes.geo.json tests/fixtures/geojson_to_json/no_geometry_1.spans.geo.json  tests/fixtures/geojson_to_json/no_geometry_1.expected.json
libcoveofds gjtoj --outputmetafilename tests/fixtures/geojson_to_json/phases_1.meta.expected.json  tests/fixtures/geojson_to_json/phases_1.nodes.geo.json tests/fixtures/geojson_to_json/phases_1.spans.geo.json  tests/fixtures/geojson_to_json/phases_1.expected.json
libcoveofds gjtoj --outputmetafilename tests/fixtures/geojson_to_json/organisations_1.meta.expected.json  tests/fixtures/geojson_to_json/organisations_1.nodes.geo.json tests/fixtures/geojson_to_json/organisations_1.spans.geo.json  tests/fixtures/geojson_to_json/organisations_1.expected.json

# JSON to GeoJSON
libcoveofds jtogj tests/fixtures/json_to_geojson/basic_1.json tests/fixtures/json_to_geojson/basic_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/basic_1.expected.spans.geo.json
libcoveofds jtogj tests/fixtures/json_to_geojson/phases_1.json tests/fixtures/json_to_geojson/phases_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/phases_1.expected.spans.geo.json
libcoveofds jtogj tests/fixtures/json_to_geojson/organisations_1.json tests/fixtures/json_to_geojson/organisations_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/organisations_1.expected.spans.geo.json
libcoveofds jtogj tests/fixtures/json_to_geojson/no_geometry_1.json tests/fixtures/json_to_geojson/no_geometry_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/no_geometry_1.expected.spans.geo.json

# JSON Schema validate
libcoveofds jsv  tests/fixtures/jsonschemavalidate/basic_1.input.json > tests/fixtures/jsonschemavalidate/basic_1.expected.json

# Python validate
# TODO
#libcoveofds pv tests/fixtures/pythonvalidate/basic_1.input.json  > tests/fixtures/pythonvalidate/basic_1.expected.json
