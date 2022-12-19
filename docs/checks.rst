Checks
======

This page describes the checks performed by the `pythonvalidate` CLI command and Python API. There are three categories of check:

* Conformance: Check that data conforms to normative rules specified in the descriptions of OFDS fields, but not otherwise encoded in the OFDS schema. For more information on the rules, see `Other normative rules <https://ofds-standard-development-handbook.readthedocs.io/en/latest/standard/schema.html#other-normative-rules>__` in the OFDS Development Handbook.
* Quality: Check other aspects of data quality.
* Informational: Check other aspects of data, not related to conformance or quality.

The CLI command and Python API return a list of check failures, each represented by a JSON object with at least the following properties:

- `type` the type of check failure
- `network_id` the `.id` of the network that failed the check
- `path` the JSON path to the field that failed the check

Some check failures include additional properties with further details of the failure, specific to the nature of the check.

Conformance checks
~~~~~~~~~~~~~~~~~~

Node reference is resolvable
----------------------------

`spans/start` and `spans/end` match the `.id` of exactly one node in the `/nodes` array.

Failure `type`:

* `span_start_node_not_found`
* `span_end_node_not_found`

Additional properties:

* `span_id`: The `.id` of the span that failed the check
* `missing_node_id`: The node reference that could not be resolved

Node location type is 'Point'
-----------------------------

`nodes/location/type` is 'Point'.

Failure `type`: `node_location_type_incorrect`

Additional properties:

- `node_id`: The `.id` of the node that failed the check
- `incorrect_type`: The `.location.type` of the node that failed the check

Node location coordinates format is a single position
-----------------------------------------------------

`nodes/location/coordinates` is a single position, i.e. an array of numbers.

Failure `type`: `node_location_coordinates_incorrect`

Additional properties:

- `node_id`: The `.id` of the node that failed the check
- `incorrect_coordinates`: The `.location.coordinates` of the node that failed the check

Span route type is 'LineString'
-------------------------------

`spans/route/type` is 'LineString'.

Failure `type`: `span_route_type_incorrect`

Additional properties:

- `span_id`: The `.id` of the span that failed the check
- `incorrect_type`: The `.location.type` of the node that failed the check

Span route coordinates is an array of positions
-----------------------------------------------

`spans/route/coordinates` is an array of positions, i.e. an array of arrays of numbers.

Failure `type`: `span_route_coordinates_incorrect`

Additional properties:

- `span_id`: The `.id` of the span that failed the check
- `incorrect_coordinates`: The `.route.coordinates` of the span that failed the check

Phase reference is resolvable
-----------------------------

`/nodes/phase/id`, `/spans/phase/id` and `/contracts/relatedPhases/id` match the `.id` of exactly one phase in the `/phases` array.

Failure `type`:

* `node_phase_reference_id_not_found`
* `span_phase_reference_id_not_found`
* `contract_related_phase_reference_id_not_found`

Additional properties:

- `node_id`, `span_id` or `contract_id`: The `.id` of the node, span or contract that failed the check
- `phase_id_not_found` the `.id` of the phase reference that could not be resolved

Phase reference name is consistent
----------------------------------

`/nodes/phase/name`, `/spans/phase/name` and `/contracts/relatedPhases/name` match the `.name` of the referenced `Phase` object in the `/phases` array.

Failure `type`:

* `node_phase_reference_name_does_not_match`
* `span_phase_reference_name_does_not_match`
* `contract_related_phase_reference_name_does_not_match`

Additional properties:

- `node_id`, `span_id` or `contract_id`: The `.id` of the node, span or contract that failed the check
- `name_in_reference`: The `.name` of the phase reference
- `name_should_be`: The `.name` of the referenced phrase

Organisation reference is resolvable
------------------------------------

The following fields match the `.id` of exactly one organisation in the `/organisations` array:

* `/nodes/physicalInfrastructureProvider/id`
* `/nodes/networkProvider/id`
* `/spans/physicalInfrastructureProvider/id`
* `/spans/networkProvider/id`
* `/spans/supplier/id`
* `/phases/funders/id`

Failure `type`:

* `node_organisation_reference_id_not_found`
* `span_organisation_reference_id_not_found`
* `phase_organisation_reference_id_not_found`

Additional properties:

- `node_id`, `span_id` or `contract_id`: The `.id` of the node, span or contract that failed the check
- `field`: The organisation reference that could not be resolved
- `organisation_id_not_found`: The `.id` of the organisation reference that could not be resolved

Organisation reference name is consistent
-----------------------------------------

The following fields match the `.name` of the referenced `Organisation` object in the `/organisations` array.

* `/nodes/physicalInfrastructureProvider/name`
* `/nodes/networkProvider/name`
* `/spans/physicalInfrastructureProvider/name`
* `/spans/networkProvider/name`
* `/spans/supplier/name`
* `/phases/funders/name`

Failure `type`:

* `node_organisation_reference_name_does_not_match`
* `span_organisation_reference_name_does_not_match`
* `phase_organisation_reference_name_does_not_match`

Additional properties:

- `node_id`, `span_id` or `phase_id`: The `.id` of the node, span or phase that failed the check
- `field`: The organisation reference whose `.name` is inconsistent
- `name_in_reference`: The `.name` of the organisation reference
- `name_should_be`: The `.name` of the referenced organisation

Node international connections country is set
-------------------------------------------------

`/nodes/internationalConnections/country` is set for each international connection in `/nodes/internationalConnections`.

Failure `type`: `node_international_connections_country_not_set`

Additional properties:

* `node_id`: The `.id` of the node that failed the check

Identifier is unique
--------------------

The following fields are unique within the scope of their parent arrays:

* `/nodes/id`
* `/spans/id`
* `/phases/id`
* `/organisations/id`
* `/contracts/id`

Failure `type`:

* `duplicate_node_id`
* `duplicate_span_id`
* `duplicate_phase_id`
* `duplicate_organisation_id`
* `duplicate_contract_id`

Additional properties:

- `node_id`, `span_id`, `phase_id`, `organisation_id` or `contract_id`: The `.id` of the node, span, phase, organisation or contract that failed the check

Quality checks
~~~~~~~~~~~~~~

Node is referenced
------------------

`nodes/id` matches the `.start` or `.end` of at least one `Span` object in the `/spans` array.

Failure `type`: `node_not_used_in_any_spans`

Additional properties:

- `node_id`: The `.id` of the node that failed the span

Informational checks
~~~~~~~~~~~~~~~~~~~~

Links to external data
----------------------

The `links` array contains a link with `.rel` set to one of the following values:

* "tag:opentelecomdata.net,2022:nodesAPI"
* "tag:opentelecomdata.net,2022:nodesFile"
* "tag:opentelecomdata.net,2022:spansAPI"
* "tag:opentelecomdata.net,2022:spansFile"

Failure `type`:

* `has_links_with_external_node_data`
* `has_links_with_external_span_data`
