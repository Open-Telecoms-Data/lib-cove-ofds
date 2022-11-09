import json
import os

import pytest

from libcoveofds.geojson import GeoJSONToJSONConverter

GEOJSON_TO_JSON_FILES = [
    # basic example
    ("basic_1"),
    # no locations / route set
    ("no_geometry_1"),
    # sort references to things correctly
    ("phases_1"),
    ("organisations_1"),
    # Check for errors in meta
    ("phases_inconsistent_1"),
    ("organisations_inconsistent_1"),
]


@pytest.mark.parametrize(
    "filename",
    GEOJSON_TO_JSON_FILES,
)
def test_geojson_to_json(filename):
    nodes_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "geojson_to_json",
        filename + ".nodes.geo.json",
    )
    spans_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "geojson_to_json",
        filename + ".spans.geo.json",
    )
    expected_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "geojson_to_json",
        filename + ".expected.json",
    )
    meta_expected_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "geojson_to_json",
        filename + ".meta.expected.json",
    )

    with open(nodes_filename) as fp:
        nodes_data = json.load(fp)
    with open(spans_filename) as fp:
        span_data = json.load(fp)

    converter = GeoJSONToJSONConverter()
    converter.process_data(nodes_data, span_data)

    with open(expected_filename) as fp:
        expected_data = json.load(fp)
    assert expected_data == converter.get_json()

    with open(meta_expected_filename) as fp:
        meta_expected_data = json.load(fp)
    assert meta_expected_data == converter.get_meta_json()
