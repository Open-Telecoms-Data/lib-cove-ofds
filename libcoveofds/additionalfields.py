from libcove2.common import get_additional_fields_info
from libcoveofds.schema import OFDSSchema


class AdditionalFields:
    def __init__(self, schema: OFDSSchema):
        self._schema = schema

    def process(self, json_data: dict) -> list:

        schema_fields = self._schema.get_package_schema_fields()

        additional_fields = get_additional_fields_info(json_data, schema_fields)

        return additional_fields
