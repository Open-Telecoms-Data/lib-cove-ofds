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
