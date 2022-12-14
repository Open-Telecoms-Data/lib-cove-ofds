import json
import os

import pytest

from libcoveofds.geojson import JSONToGeoJSONConverter

JSON_TO_GEOJSON_FILES = [
    # basic example
    ("basic_1"),
    # with phases - check dereffed
    ("phases_1"),
    ("phase_funders"),
    # Organisations derefed
    ("organisations_1"),
    # no locations / route set
    ("no_geometry_1"),
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
    expected_spans_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".expected.spans.geo.json",
    )
    expected_nodes_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".expected.nodes.geo.json",
    )
    meta_expected_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        filename + ".expected.meta.json",
    )

    with open(json_filename) as fp:
        json_data = json.load(fp)

    converter = JSONToGeoJSONConverter()
    converter.process_package(json_data)

    with open(expected_spans_filename) as fp:
        expected_spans_data = json.load(fp)
    assert expected_spans_data == converter.get_spans_geojson()

    with open(expected_nodes_filename) as fp:
        expected_nodes_data = json.load(fp)
    assert expected_nodes_data == converter.get_nodes_geojson()

    with open(meta_expected_filename) as fp:
        meta_expected_data = json.load(fp)
    assert meta_expected_data == converter.get_meta_json()


def test_dont_crash_1():
    """Just put as much bad stuff as possible in the input and make sure it doesn't crash!
    We don't care about testing output. Other tests can do that."""
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "json_to_geojson",
        "dont_crash_1.json",
    )

    with open(json_filename) as fp:
        json_data = json.load(fp)

    converter = JSONToGeoJSONConverter()
    converter.process_package(json_data)
