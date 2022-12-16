Command-Line Interface
======================

To see all commands, run:

.. code-block:: bash

    libcoveofds --help


Commands
~~~~~~~~

To see the options for each command, run:

.. code-block:: bash

    libcoveofds commandname --help


jsonschemavalidate
------------------

Validate data against the OFDS schema.

Mandatory positional arguments:

- `inputfilename` File name of an input JSON data file

.. code-block:: bash

    libcoveofds  jsonschemavalidate data.json

For the Python API, see :meth:`libcoveofds.jsonschemavalidate.JSONSchemaValidator`.
