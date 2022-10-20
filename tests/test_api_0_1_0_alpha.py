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
    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "missing_node_id": "167",
        "type": "span_start_node_not_found",
    }


def test_start_node_not_found_but_has_external_nodes_1():
    """This data file has external nodes, so we can't check that links have a start.
    Make sure that error doesn't appear.
    But look for has_related_resources which should appear."""

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "start_node_not_found_but_has_external_nodes_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    print(results["additional_checks"])

    assert results["additional_checks_count"] == 1

    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "type": "has_links_with_external_node_data",
    }


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
    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "missing_node_id": "2467",
        "type": "span_end_node_not_found",
    }


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
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "1",
        "type": "node_location_type_incorrect",
    }


def test_span_route_type_incorrect_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "span_route_type_incorrect_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "type": "span_route_type_incorrect",
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
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "1",
        "type": "node_location_coordinates_incorrect",
    }


def test_span_route_coordinates_incorrect_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "span_route_coordinates_incorrect_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "type": "span_route_coordinates_incorrect",
    }


def test_phase_id_not_found_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "phase_id_not_found_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 3

    # Library is not meant to return these in any special order, so sort by type to get something we can check.
    additional_checks = sorted(results["additional_checks"], key=lambda d: d["type"])

    assert additional_checks[0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "contract_id": "1",
        "type": "contract_related_phase_reference_id_not_found",
    }
    assert additional_checks[1] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "1",
        "type": "node_phase_reference_id_not_found",
    }
    assert additional_checks[2] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "type": "span_phase_reference_id_not_found",
    }


def test_phase_name_not_match_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "phase_name_not_match_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 3

    # Library is not meant to return these in any special order, so sort by type to get something we can check.
    additional_checks = sorted(results["additional_checks"], key=lambda d: d["type"])

    assert additional_checks[0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "contract_id": "1",
        "type": "contract_related_phase_reference_name_does_not_match",
    }
    assert additional_checks[1] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "1",
        "type": "node_phase_reference_name_does_not_match",
    }
    assert additional_checks[2] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "type": "span_phase_reference_name_does_not_match",
    }


def test_phase_reference_name_set_but_not_in_original_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "phase_reference_name_set_but_not_in_original_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 4

    # Library is not meant to return these in any special order, so sort by type to get something we can check.
    additional_checks = sorted(results["additional_checks"], key=lambda d: d["type"])

    assert additional_checks[0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "contract_id": "1",
        "type": "contract_related_phase_reference_name_set_but_not_in_original",
    }
    assert additional_checks[1] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "1",
        "type": "node_phase_reference_name_set_but_not_in_original",
    }
    assert additional_checks[2] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "2",
        "type": "node_phase_reference_name_set_but_not_in_original",
    }
    assert additional_checks[3] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "span_id": "1",
        "type": "span_phase_reference_name_set_but_not_in_original",
    }


def test_node_international_connections_country_not_set_1():

    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "node_international_connections_country_not_set_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "1",
        "type": "node_international_connections_country_not_set",
    }


def test_node_not_used_in_any_spans_1():
    cove_temp_folder = tempfile.mkdtemp(
        prefix="lib-cove-ofds-tests-", dir=tempfile.gettempdir()
    )
    json_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "0_1_0_alpha",
        "node_not_used_in_any_spans_1.json",
    )

    results = ofds_json_output(cove_temp_folder, json_filename)

    assert results["schema_version"] == "0.1.0-alpha"

    assert results["validation_errors_count"] == 0

    assert results["additional_checks_count"] == 1
    assert results["additional_checks"][0] == {
        "network_id": "a096d627-72e1-4f9b-b129-951b1737bff4",
        "node_id": "3",
        "type": "node_not_used_in_any_spans",
    }
