# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- JSONSchema validate:
  - Add format checkers

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
