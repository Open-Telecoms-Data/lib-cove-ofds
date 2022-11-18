Additional Checks
=================


Spans must have valid start and end nodes
-----------------------------------------

Produces additional checks of types:

* `span_start_node_not_found`
* `span_end_node_not_found`


Nodes location check
--------------------

Checks type is correct (`Point`) and coordinates are correct (a single pair).

Produces additional checks of types:

* `node_location_type_incorrect`
* `node_location_coordinates_incorrect`

Spans route check
-----------------

Checks type is correct (`LineString`) and coordinates are correct (a list).

Produces additional checks of types:

* `span_route_type_incorrect`
* `span_route_coordinates_incorrect`

Phase reference checks
----------------------

Checks referenced phases exist.

If a name is given in the reference, check it matches the name of the phase exactly.

Also raises an alert if a name is given in the phase reference but not the phase.

Produces additional checks of types:

* `node_phase_reference_id_not_found`
* `node_phase_reference_name_does_not_match`
* `node_phase_reference_name_set_but_not_in_original`
* `span_phase_reference_id_not_found`
* `span_phase_reference_name_does_not_match`
* `span_phase_reference_name_set_but_not_in_original`
* `contract_related_phase_reference_id_not_found`
* `contract_related_phase_reference_name_does_not_match`
* `contract_related_phase_reference_name_set_but_not_in_original`

Organisation reference checks
-----------------------------

Checks referenced organisations exist.

If a name is given in the reference, check it matches the name of the organisation exactly.

Also raises an alert if a name is given in the organisation reference but not the organisation.

Produces additional checks of types:

* `node_organisation_reference_id_not_found`
* `node_organisation_reference_name_does_not_match`
* `node_organisation_reference_name_set_but_not_in_original`
* `span_organisation_reference_id_not_found`
* `span_organisation_reference_name_does_not_match`
* `span_organisation_reference_name_set_but_not_in_original`
* `phase_organisation_reference_id_not_found`
* `phase_organisation_reference_name_does_not_match`
* `phase_organisation_reference_name_set_but_not_in_original`

Node internationalConnections Country must be set
-------------------------------------------------

Produces additional checks of type:

* `node_international_connections_country_not_set`

Has links with external data
----------------------------

Produces additional checks of type:

* `has_links_with_external_node_data`
* `has_links_with_external_span_data`

Node not used in any spans
--------------------------

Produces additional checks of type:

* `node_not_used_in_any_spans`

Unique ID's
-----------

* `duplicate_node_id`
* `duplicate_span_id`
* `duplicate_phase_id`
* `duplicate_organisation_id`
* `duplicate_contract_id`

