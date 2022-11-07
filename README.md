# Lib Cove OFDS

See https://libcoveofds.readthedocs.io/en/latest/ for docs.

## Command line

### Installation

Installation from this git repo:

```bash
git clone https://github.com/Open-Telecoms-Data/lib-cove-ofds.git
cd lib-cove-ofds
python3 -m venv .ve
source .ve/bin/activate
pip install -e .
```

### Running the command line tool

Call `libcoveofds` and pass the filename of some JSON data.

    libcoveofds tests/fixtures/0.1/basic_1.json
    
You can also pass the raw option to see the JSON as it originally came out of the library.

    libcoveofds --raw tests/fixtures/0.1/basic_1.json

### Running tests

    python -m pytest

### Code linting

Make sure dev dependencies are installed in your virtual environment:

    pip install -e .[dev]

Then run:

    isort libcoveofds/ libcove2/ tests/ setup.py
    black libcoveofds/ libcove2/ tests/ setup.py
    flake8 libcoveofds/ libcove2/ tests/ setup.py
    mypy --install-types --non-interactive -p  libcoveofds

