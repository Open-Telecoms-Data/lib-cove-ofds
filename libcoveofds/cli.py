import argparse
import json

import libcoveofds.python_validate
import libcoveofds.schema


def main():
    parser = argparse.ArgumentParser(description="Lib Cove OFDS CLI")
    subparsers = parser.add_subparsers(dest="subparser_name")

    python_validate_parser = subparsers.add_parser("pythonvalidate", aliases=["pv"])
    python_validate_parser.add_argument(
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


if __name__ == "__main__":
    main()
