import json
import os
import tempfile

from libcoveofds.api import ofds_json_output


def test_basic_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "basic_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"
    assert results["validation_errors_count"] == 0
    assert results["additional_checks_count"] == 0


def test_validation_errors_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "validation_errors_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 1

    validation_error: dict = json.loads(results["validation_errors"][0][0])
    assert (
        validation_error["message"]
        == "'nodes' should be a JSON array. Check that value(s) appear within square brackets, [...]"
    )

    assert results["additional_checks_count"] == 0


def test_start_node_not_found_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "start_node_not_found_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0]["type"] == "link_start_node_not_found"


def test_end_node_not_found_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "end_node_not_found_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0]["type"] == "link_end_node_not_found"


def test_node_location_type_incorrect_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "node_location_type_incorrect_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "node_id": "1",
        "type": "node_location_type_incorrect",
    }


def test_link_route_type_incorrect_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "link_route_type_incorrect_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "link_id": "1",
        "type": "link_route_type_incorrect",
    }


def test_node_location_coordinates_incorrect_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "node_location_coordinates_incorrect_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "node_id": "1",
        "type": "node_location_coordinates_incorrect",
    }


def test_link_route_coordinates_incorrect_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "link_route_coordinates_incorrect_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "link_id": "1",
        "type": "link_route_coordinates_incorrect",
    }
