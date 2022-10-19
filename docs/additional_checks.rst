Additional Checks
=================


Links must have valid start and end nodes
-----------------------------------------

Produces additional checks of types:

* `link_start_node_not_found`
* `link_end_node_not_found`


Nodes location check
--------------------

Checks type is correct (`Point`) and coordinates are correct (a single pair).

Produces additional checks of types:

* `node_location_type_incorrect`
* `node_location_coordinates_incorrect`

Links route check
-----------------

Checks type is correct (`LineString`) and coordinates are correct (a list).

Produces additional checks of types:

* `link_route_type_incorrect`
* `link_route_coordinates_incorrect`

Phase reference checks
----------------------

Checks referenced phases exist.

If a name is given in the reference, check it matches the name of the phase exactly.

Also raises an alert if a name is given in the phase reference but not the phase.

Produces additional checks of types:

* `node_phase_reference_id_not_found`
* `node_phase_reference_name_does_not_match`
* `node_phase_reference_name_set_but_not_in_original`
* `link_phase_reference_id_not_found`
* `link_phase_reference_name_does_not_match`
* `link_phase_reference_name_set_but_not_in_original`
* `contract_related_phase_reference_id_not_found`
* `contract_related_phase_reference_name_does_not_match`
* `contract_related_phase_reference_name_set_but_not_in_original`

Node internationalConnections Country must be set
-------------------------------------------------

Produces additional checks of type:

* `node_international_connections_country_not_set`

Has links with external data
----------------------------

Produces additional checks of type:

* `has_related_resources`
