import argparse
import json

import libcoveofds.additionalfields
import libcoveofds.jsonschemavalidate
import libcoveofds.python_validate
import libcoveofds.schema


def main():
    parser = argparse.ArgumentParser(description="Lib Cove OFDS CLI")
    subparsers = parser.add_subparsers(dest="subparser_name")

    python_validate_parser = subparsers.add_parser("pythonvalidate", aliases=["pv"])
    python_validate_parser.add_argument(
        "inputfilename", help="File name of an input JSON data file"
    )

    additional_fields_parser = subparsers.add_parser("additionalfields", aliases=["af"])
    additional_fields_parser.add_argument(
        "inputfilename", help="File name of an input JSON data file"
    )

    json_schema_validate_parser = subparsers.add_parser(
        "jsonschemavalidate", aliases=["jsv"]
    )
    json_schema_validate_parser.add_argument(
        "inputfilename", help="File name of an input JSON data file"
    )

    args = parser.parse_args()

    if args.subparser_name == "pythonvalidate" or args.subparser_name == "pv":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        schema = libcoveofds.schema.OFDSSchema()
        validator = libcoveofds.python_validate.PythonValidate(schema)

        output = validator.validate(input_data)

        print(json.dumps(output, indent=4))

    elif args.subparser_name == "additionalfields" or args.subparser_name == "af":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        schema = libcoveofds.schema.OFDSSchema()
        validator = libcoveofds.additionalfields.AdditionalFields(schema)

        output = validator.process(input_data)

        print(json.dumps(output, indent=4))

    elif args.subparser_name == "jsonschemavalidate" or args.subparser_name == "jsv":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        schema = libcoveofds.schema.OFDSSchema()
        validators = libcoveofds.jsonschemavalidate.JSONSchemaValidator(schema)

        output = validators.validate(input_data)

        output_json = [o.json() for o in output]

        print(json.dumps(output_json, indent=4))


if __name__ == "__main__":
    main()
