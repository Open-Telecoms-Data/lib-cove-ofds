Command-Line Interface
======================

To see all commands, run:

.. code-block:: bash

    libcoveofds --help


To see the options for each command, run:

.. code-block:: bash

    libcoveofds commandname --help


The abbreviated alias for each command is shown in brackets.

jsonschemavalidate (jsv)
------------------------

Validates data against the OFDS schema and returns a list of validation errors.

For more information, see `handling validation errors <https://python-jsonschema.readthedocs.io/en/latest/errors/#handling-validation-errors>`__ in the jsonschema library documentation.

Mandatory positional arguments:

- ``inputfilename`` File name of an input JSON data file

.. code-block:: bash

    libcoveofds jsonschemavalidate data.json

pythonvalidate (pv)
-------------------

Performs conformance, quality and informational checks, and returns a list of check failures.

For more information on the checks and failures, see :doc:`checks`.

Mandatory positional arguments:

- ``inputfilename`` File name of an input JSON data file

.. code-block:: bash

    libcoveofds pythonvalidate data.json

additionalfields (af)
---------------------

Checks for additional fields not specified in the schema and returns a list of additional fields.

For more information on the output format returned by the command, see :doc: `additional_fields`.

Mandatory positional arguments:

- ``inputfilename`` File name of an input JSON data file

.. code-block:: bash

    libcoveofds additionalfields data.json

jsontogeojson (jtogj)
---------------------

Converts data from JSON format to GeoJSON format.

For more information on the input and output formats, see the `JSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/json.html>`__ and the `GeoJSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/geojson.html>`__.

Mandatory positional arguments:

- ``inputfilename`` File name of an input JSON data file
- ``outputnodesfilename`` Output filename to write Nodes GeoJSON data to
- ``outputspansfilename`` Output filename to write Spans GeoJSON data to

.. code-block:: bash

    libcoveofds jsontogeojson data.json

geojsontojson (gjtoj)
---------------------

Converts data from GeoJSON to JSON format.

For more information on the input and output formats, see the `GeoJSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/geojson.html>`__ and the `JSON publication format reference <https://open-fibre-data-standard.readthedocs.io/en/latest/reference/publication_formats/json.html>`__.

Mandatory positional arguments:

- ``inputnodesfilename`` File name of an input Nodes GeoJSON data file
- ``inputspansfilename`` File name of an input Spans GeoJSON data file
- ``outputfilename`` Output filename to write JSON data to

.. code-block:: bash

    libcoveofds geojsontojson data.json
