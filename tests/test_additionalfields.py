import json
import os

import pytest

from libcoveofds.additionalfields import AdditionalFields
from libcoveofds.schema import OFDSSchema

ADDITIONAL_FIELDS_FILES = [
    ("basic_1"),
]


@pytest.mark.parametrize(
    "filename",
    ADDITIONAL_FIELDS_FILES,
)
def test_additional_fields_1(filename):
    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "additionalfields",
        filename + ".input.json",
    )
    expected_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "additionalfields",
        filename + ".expected.json",
    )

    with open(input_filename) as fp:
        input_data = json.load(fp)
    with open(expected_filename) as fp:
        expected_data = json.load(fp)

    schema = OFDSSchema()
    processor = AdditionalFields(schema)
    output = processor.process(input_data)

    assert expected_data == output
