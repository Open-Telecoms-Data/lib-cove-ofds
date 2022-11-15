# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Updated schema to 0__1__0__beta

### Added

- JSON to GeoJSON:
  - [#31](https://github.com/Open-Telecoms-Data/lib-cove-ofds/pull/31) - `jsontogeojson`: Dereference funders
- Python Validate:
  - add more information to errors

## [0.4.0] - 2022-11-09

### Added

- JSONSchema validate:
  - Add format checkers
  - Add more fields to output object
- GeoJSON to JSON:
  - meta information includes inconsistent ids on organisations and phases
- JSON to GeoJSON:
  - add any_spans_with_geometry and any_nodes_with_geometry to meta
- Python Validate:
  - add more information to errors

## [0.3.0] - 2022-11-08

### Added

- GeoJSON to JSON and JSON to GeoJSON conversion
- Improved in GeoJSON to JSON:
    - Makes Phases into references & populates phases array (Nodes, Spans)
    - Makes Organisations into references & populates organisations array (Nodes, Spans)
    - Add meta output, with output field coverage
    - Fix bug that meant get_json() could not be called twice
    - Include contracts
- Improved in JSON to GeoJSON:
    - Add meta output, with output field coverage

### Changed

- Schema object - change properties and methods to have both package schema and data schema
- Update to the latest version of the schema.

## [0.2.0] - 2022-11-03

### Changed

**REFACTOR!**

- Remove dependency on libcove and libcoveweb
- Remove other code for cove - the ways cove will call Python API's in this library changes
- Rename common checks to python validate and change API slightly
- CLI has sub arguments 


## [0.1.0] - 2022-10-27

- First Release
