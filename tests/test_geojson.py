import json
import os
import tempfile

import pytest

from libcoveofds.api import ofds_json_output
from libcoveofds.lib.geojson import JSONToGeoJSONConverter

JSON_TO_GEOJSON_FILES = [
    # basic example
    ("basic_1"),
    # with phases - check dereffed
    ("phases_1"),
    # Organisations derefed
    ("organisations_1"),
]


@pytest.mark.parametrize(
    "filename",
    JSON_TO_GEOJSON_FILES,
)
def test_json_to_geojson(filename):
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".json",
    )
    expected_links_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".expected.links.geo.json",
    )
    expected_nodes_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".expected.nodes.geo.json",
    )

    with open(json_filename) as fp:
        json_data = json.load(fp)

    converter = JSONToGeoJSONConverter()
    converter.process_package(json_data)

    # When writing tests, these can be handy
    # with open(expected_nodes_filename, "w") as fp:
    #    json.dump(converter.get_nodes_geojson(), fp, indent=4)
    # with open(expected_links_filename, "w") as fp:
    #    json.dump(converter.get_links_geojson(), fp, indent=4)

    with open(expected_links_filename) as fp:
        expected_links_data = json.load(fp)
    assert expected_links_data == converter.get_links_geojson()

    with open(expected_nodes_filename) as fp:
        expected_nodes_data = json.load(fp)
    assert expected_nodes_data == converter.get_nodes_geojson()


@pytest.mark.parametrize(
    "filename",
    JSON_TO_GEOJSON_FILES,
)
def test_json_to_geojson_inputs_valid(filename):

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["validation_errors_count"] == 0
    assert results["additional_checks_count"] == 0
