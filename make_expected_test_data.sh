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
libcoveofds gjtoj --outputmetafilename tests/fixtures/geojson_to_json/phases_inconsistent_1.meta.expected.json  tests/fixtures/geojson_to_json/phases_inconsistent_1.nodes.geo.json tests/fixtures/geojson_to_json/phases_inconsistent_1.spans.geo.json  tests/fixtures/geojson_to_json/phases_inconsistent_1.expected.json
libcoveofds gjtoj --outputmetafilename tests/fixtures/geojson_to_json/organisations_inconsistent_1.meta.expected.json  tests/fixtures/geojson_to_json/organisations_inconsistent_1.nodes.geo.json tests/fixtures/geojson_to_json/organisations_inconsistent_1.spans.geo.json  tests/fixtures/geojson_to_json/organisations_inconsistent_1.expected.json

# JSON to GeoJSON
libcoveofds jtogj --outputmetafilename tests/fixtures/json_to_geojson/basic_1.expected.meta.json tests/fixtures/json_to_geojson/basic_1.json tests/fixtures/json_to_geojson/basic_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/basic_1.expected.spans.geo.json
libcoveofds jtogj --outputmetafilename tests/fixtures/json_to_geojson/phases_1.expected.meta.json tests/fixtures/json_to_geojson/phases_1.json tests/fixtures/json_to_geojson/phases_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/phases_1.expected.spans.geo.json
libcoveofds jtogj --outputmetafilename tests/fixtures/json_to_geojson/organisations_1.expected.meta.json tests/fixtures/json_to_geojson/organisations_1.json tests/fixtures/json_to_geojson/organisations_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/organisations_1.expected.spans.geo.json
libcoveofds jtogj --outputmetafilename tests/fixtures/json_to_geojson/no_geometry_1.expected.meta.json tests/fixtures/json_to_geojson/no_geometry_1.json tests/fixtures/json_to_geojson/no_geometry_1.expected.nodes.geo.json tests/fixtures/json_to_geojson/no_geometry_1.expected.spans.geo.json
libcoveofds jtogj --outputmetafilename tests/fixtures/json_to_geojson/phase_funders.expected.meta.json tests/fixtures/json_to_geojson/phase_funders.json tests/fixtures/json_to_geojson/phase_funders.expected.nodes.geo.json tests/fixtures/json_to_geojson/phase_funders.expected.spans.geo.json

# JSON Schema validate
libcoveofds jsv  tests/fixtures/jsonschemavalidate/basic_1.input.json > tests/fixtures/jsonschemavalidate/basic_1.expected.json
libcoveofds jsv  tests/fixtures/jsonschemavalidate/bad_uuid_1.input.json > tests/fixtures/jsonschemavalidate/bad_uuid_1.expected.json

# Python validate
libcoveofds pv tests/fixtures/pythonvalidate/basic_1.input.json  > tests/fixtures/pythonvalidate/basic_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/end_node_not_found_1.input.json  > tests/fixtures/pythonvalidate/end_node_not_found_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/node_international_connections_country_not_set_1.input.json  > tests/fixtures/pythonvalidate/node_international_connections_country_not_set_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/node_location_coordinates_incorrect_1.input.json  > tests/fixtures/pythonvalidate/node_location_coordinates_incorrect_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/node_location_type_incorrect_1.input.json  > tests/fixtures/pythonvalidate/node_location_type_incorrect_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/node_not_used_in_any_spans_1.input.json  > tests/fixtures/pythonvalidate/node_not_used_in_any_spans_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/organisation_id_not_found_1.input.json  > tests/fixtures/pythonvalidate/organisation_id_not_found_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/organisation_name_not_match_1.input.json  > tests/fixtures/pythonvalidate/organisation_name_not_match_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/organisation_reference_name_set_but_not_in_original_1.input.json  > tests/fixtures/pythonvalidate/organisation_reference_name_set_but_not_in_original_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/phase_id_not_found_1.input.json  > tests/fixtures/pythonvalidate/phase_id_not_found_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/phase_name_not_match_1.input.json  > tests/fixtures/pythonvalidate/phase_name_not_match_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/phase_reference_name_set_but_not_in_original_1.input.json  > tests/fixtures/pythonvalidate/phase_reference_name_set_but_not_in_original_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/span_route_coordinates_incorrect_1.input.json  > tests/fixtures/pythonvalidate/span_route_coordinates_incorrect_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/span_route_type_incorrect_1.input.json  > tests/fixtures/pythonvalidate/span_route_type_incorrect_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/start_node_not_found_1.input.json  > tests/fixtures/pythonvalidate/start_node_not_found_1.expected.json
libcoveofds pv tests/fixtures/pythonvalidate/start_node_not_found_but_has_external_nodes_1.input.json  > tests/fixtures/pythonvalidate/start_node_not_found_but_has_external_nodes_1.expected.json