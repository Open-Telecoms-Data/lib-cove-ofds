Contributing
============

Installing dev tools
--------------------

You need to install the `dev` extras.

For instance, to checkout the repository, create a virtual environment and install the dev tools:

.. code-block:: bash

    git clone https://github.com/Open-Telecoms-Data/lib-cove-ofds.git
    cd lib-cove-ofds
    python3 -m venv .ve
    source .ve/bin/activate
    pip install -e .[dev]

Running tests
-------------

.. code-block:: bash

    python -m pytest

For writing tests, look in `make_expected_test_data.sh` for a helper script.

Code linting
------------

Then run:

.. code-block:: bash

    isort libcoveofds/ libcove2/ tests/ setup.py
    black libcoveofds/ libcove2/ tests/ setup.py
    flake8 libcoveofds/ libcove2/ tests/ setup.py
    mypy --install-types --non-interactive -p  libcoveofds

Building new schema files
-------------------------

Check out the data standard repository. Make sure it is on the correct tag, branch or commit you want.

Install https://pypi.org/project/compiletojsonschema/ version 0.5 or ahove

At this stage you may need to edit the schema files by hand.
The `network-package-schema.json` file may refer to a `network-schema.json` file on GitHub, not locally.
In this case change the `$id` and `$ref` to refer to the correct tag you want, or to refer to the local file.

Change to the directory of the data standard repository, then run:

.. code-block:: bash

    compiletojsonschema -c codelists/closed/   schema/network-package-schema.json  >  ~/WHEREVER/libcoveofds/data/schema-X-Y-Z.json
    compiletojsonschema -c codelists/closed/   schema/network-schema.json  >  ~/WHEREVER/openfibre-lib-cove/libcoveofds/data/schema-X-Y-Z-network-only.json

