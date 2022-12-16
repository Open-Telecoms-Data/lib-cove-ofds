Lib CoVE OFDS
=============

A command-line tool and Python library for to convert, validate and explore Open Fibre Data Standard (OFDS) data:

- Validate data against the schema
- Check that data conforms to normative rules specified in OFDS
- Report additional fields not specified in the schema
- Convert data from JSON format to GeoJSON format
- Convert data from GeoJSON to JSON format

Installation
~~~~~~~~~~~~

Clone the repository:

.. code-block:: bash

    git clone https://github.com/Open-Telecoms-Data/lib-cove-ofds.git

Create and activate a virtual environment:

.. code-block:: bash
    cd lib-cove-ofds
    python3 -m venv .ve
    source .ve/bin/activate

Install:

.. code-block:: bash
    pip install .

Contents
~~~~~~~~

.. toctree::
   :maxdepth: 2

   json_schema_validate.rst
   python_validate.rst
   additional_fields.rst
   json_to_geojson.rst
   geojson_to_json.rst
