from libcoveofds.config import LibCoveOFDSConfig
from libcoveofds.schema import SchemaOFDS


class AdditionalCheckForNetwork:
    """Any check or statistic that wants to be provided should extend this abstract class and overwrite methods"""

    def __init__(
        self, lib_cove_ofds_config: LibCoveOFDSConfig, schema_object: SchemaOFDS
    ):
        self._additional_check_results: list = []
        self.lib_cove_ofds_config: LibCoveOFDSConfig = lib_cove_ofds_config
        self._schema_object: SchemaOFDS = schema_object

    def check_node_first_pass(self, node: dict):
        pass

    def check_link_first_pass(self, link: dict):
        pass

    def check_phase_first_pass(self, phase: dict):
        pass

    def check_organisation_first_pass(self, organisation: dict):
        pass

    def check_contract_first_pass(self, contract: dict):
        pass

    def check_node_second_pass(self, node: dict):
        pass

    def check_link_second_pass(self, link: dict):
        pass

    def check_phase_second_pass(self, phase: dict):
        pass

    def check_organisation_second_pass(self, organisation: dict):
        pass

    def check_contract_second_pass(self, contract: dict):
        pass

    def get_additional_check_results(self):
        return self._additional_check_results

    def skip_if_any_related_resources(self) -> bool:
        pass


class LinksMustHaveValidNodesAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, lib_cove_bods_config, schema_object):
        super().__init__(lib_cove_bods_config, schema_object)
        self._node_ids_seen = []

    def check_node_first_pass(self, node: dict):
        id = node.get("id")
        if id:
            self._node_ids_seen.append(id)

    def check_link_second_pass(self, link: dict):
        link_id = link.get("id")
        start = link.get("start")
        if start:
            self._check_node_id_valid(start, "link_start_node_not_found", link_id)
        end = link.get("end")
        if end:
            self._check_node_id_valid(end, "link_end_node_not_found", link_id)

    def _check_node_id_valid(self, node_id, error_type, link_id):
        if not node_id in self._node_ids_seen:
            self._additional_check_results.append(
                {"type": error_type, "missing_node_id": node_id, "link_id": link_id}
            )

    def skip_if_any_related_resources(self) -> bool:
        return True


class NodesLocationAndLinksRouteAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def check_node_first_pass(self, node: dict):
        location = node.get("location")
        if location:
            type = location.get("type")
            if type != "Point":
                self._additional_check_results.append(
                    {"type": "node_location_type_incorrect", "node_id": node.get("id")}
                )
            if not self._is_json_coordinates(location.get("coordinates")):
                self._additional_check_results.append(
                    {
                        "type": "node_location_coordinates_incorrect",
                        "node_id": node.get("id"),
                    }
                )

    def check_link_first_pass(self, link: dict):
        location = link.get("route")
        if location:
            type = location.get("type")
            if type != "LineString":
                self._additional_check_results.append(
                    {"type": "link_route_type_incorrect", "link_id": link.get("id")}
                )
            if not self._is_json_list_coordinates(location.get("coordinates")):
                self._additional_check_results.append(
                    {
                        "type": "link_route_coordinates_incorrect",
                        "link_id": link.get("id"),
                    }
                )

    def _is_json_list_coordinates(self, list_coordinates):
        if not isinstance(list_coordinates, list):
            return False
        for coordinates in list_coordinates:
            if not self._is_json_coordinates(coordinates):
                return False
        return True

    def _is_json_coordinates(self, coordinates):
        return (
            isinstance(coordinates, list)
            and len(coordinates) == 2
            and (isinstance(coordinates[0], float) or isinstance(coordinates[0], int))
            and (isinstance(coordinates[1], float) or isinstance(coordinates[1], int))
        )

    def skip_if_any_related_resources(self) -> bool:
        return False


class PhaseReferenceAdditionalCheckForNetwork(AdditionalCheckForNetwork):
    def __init__(self, lib_cove_bods_config, schema_object):
        super().__init__(lib_cove_bods_config, schema_object)
        self._phases: dict = {}

    def check_phase_first_pass(self, phase: dict):
        id = phase.get("id")
        name = phase.get("name")
        if id:
            self._phases[id] = name

    def check_node_second_pass(self, node: dict):
        if "phase" in node and isinstance(node["phase"], dict):
            self._check_related_phase_object(
                node["phase"],
                {
                    "type": "node_phase_reference_id_not_found",
                    "node_id": node.get("id"),
                },
                {
                    "type": "node_phase_reference_name_does_not_match",
                    "node_id": node.get("id"),
                },
                {
                    "type": "node_phase_reference_name_set_but_not_in_original",
                    "node_id": node.get("id"),
                },
            )

    def check_link_second_pass(self, link: dict):
        if "phase" in link and isinstance(link["phase"], dict):
            self._check_related_phase_object(
                link["phase"],
                {
                    "type": "link_phase_reference_id_not_found",
                    "link_id": link.get("id"),
                },
                {
                    "type": "link_phase_reference_name_does_not_match",
                    "link_id": link.get("id"),
                },
                {
                    "type": "link_phase_reference_name_set_but_not_in_original",
                    "link_id": link.get("id"),
                },
            )

    def check_contract_second_pass(self, contract: dict):
        if "relatedPhases" in contract and isinstance(contract["relatedPhases"], list):
            for related_phase in contract["relatedPhases"]:
                if isinstance(related_phase, dict):
                    self._check_related_phase_object(
                        related_phase,
                        {
                            "type": "contract_related_phase_reference_id_not_found",
                            "contract_id": contract.get("id"),
                        },
                        {
                            "type": "contract_related_phase_reference_name_does_not_match",
                            "contract_id": contract.get("id"),
                        },
                        {
                            "type": "contract_related_phase_reference_name_set_but_not_in_original",
                            "contract_id": contract.get("id"),
                        },
                    )

    def _check_related_phase_object(
        self,
        related_phase: dict,
        id_not_found_result: dict,
        name_not_match_result: dict,
        name_set_but_not_in_original_result: dict,
    ):
        id = related_phase.get("id")
        name = related_phase.get("name")
        # id is required in JSON Schema - if it is not set we can let that validation raise an error.
        # We'll only carry on with our checks (those that can't be done in JSON Schema) if id exists.
        if id:
            if id in self._phases:
                # check - if name is set on reference but not on original
                if name and not self._phases[id]:
                    self._additional_check_results.append(
                        name_set_but_not_in_original_result
                    )
                # check - if names are both set, do they match?
                if name and self._phases[id] and name != self._phases[id]:
                    self._additional_check_results.append(name_not_match_result)
            else:
                # check failed - id is not known
                self._additional_check_results.append(id_not_found_result)

    def skip_if_any_related_resources(self) -> bool:
        return False


class NodeInternationalConnectionCountryAdditionalCheckForNetwork(
    AdditionalCheckForNetwork
):
    def check_node_first_pass(self, node: dict):
        if "internationalConnections" in node and isinstance(
            node["internationalConnections"], list
        ):
            for international_connection in node["internationalConnections"]:
                if isinstance(
                    international_connection, dict
                ) and not international_connection.get("country"):
                    self._additional_check_results.append(
                        {
                            "type": "node_international_connections_country_not_set",
                            "node_id": node.get("id"),
                        }
                    )

    def skip_if_any_related_resources(self) -> bool:
        return False


ADDITIONAL_CHECK_CLASSES_FOR_NETWORK = [
    LinksMustHaveValidNodesAdditionalCheckForNetwork,
    NodesLocationAndLinksRouteAdditionalCheckForNetwork,
    PhaseReferenceAdditionalCheckForNetwork,
    NodeInternationalConnectionCountryAdditionalCheckForNetwork,
]


def process_additional_checks(
    json_data: dict, lib_cove_ofds_config: LibCoveOFDSConfig, schema_object: SchemaOFDS
):
    additional_checks: list = []
    statistics: dict = {}

    # For each Network
    networks = json_data.get("networks")
    if isinstance(networks, list):
        for network in networks:
            if isinstance(network, dict):
                additional_check_instances = [
                    x(lib_cove_ofds_config, schema_object)
                    for x in ADDITIONAL_CHECK_CLASSES_FOR_NETWORK
                ]
                related_resources = network.get("relatedResources", [])
                if related_resources:
                    additional_check_instances = [
                        x
                        for x in additional_check_instances
                        if not x.skip_if_any_related_resources()
                    ]
                    additional_checks.append(
                        {
                            "network_id": network.get("id"),
                            "type": "has_related_resources",
                        }
                    )
                nodes = network.get("nodes", [])
                nodes = nodes if isinstance(nodes, list) else []
                links = network.get("links", [])
                links = links if isinstance(links, list) else []
                phases = network.get("phases", [])
                phases = phases if isinstance(phases, list) else []
                organisations = network.get("organisations", [])
                organisations = organisations if isinstance(organisations, list) else []
                contracts = network.get("contracts", [])
                contracts = contracts if isinstance(contracts, list) else []
                # First pass
                for additional_check_instance in additional_check_instances:
                    for node in nodes:
                        additional_check_instance.check_node_first_pass(node)
                    for link in links:
                        additional_check_instance.check_link_first_pass(link)
                    for phase in phases:
                        additional_check_instance.check_phase_first_pass(phase)
                    for organisation in organisations:
                        additional_check_instance.check_organisation_first_pass(
                            organisation
                        )
                    for contract in contracts:
                        additional_check_instance.check_contract_first_pass(contract)
                # Second pass
                for additional_check_instance in additional_check_instances:
                    for node in nodes:
                        additional_check_instance.check_node_second_pass(node)
                    for link in links:
                        additional_check_instance.check_link_second_pass(link)
                    for phase in phases:
                        additional_check_instance.check_phase_second_pass(phase)
                    for organisation in organisations:
                        additional_check_instance.check_organisation_second_pass(
                            organisation
                        )
                    for contract in contracts:
                        additional_check_instance.check_contract_second_pass(contract)
                # Results
                for additional_check_instance in additional_check_instances:
                    for (
                        additional_check
                    ) in additional_check_instance.get_additional_check_results():
                        additional_check["network_id"] = network.get("id")
                        additional_checks.append(additional_check)

    # Return
    return {"additional_checks": additional_checks, "statistics": statistics}
