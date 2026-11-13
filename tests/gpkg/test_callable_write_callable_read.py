import os
import shutil
import sqlite3
import tempfile

import pytest

import libcoveofds.gpkg.from_json


def test_security(monkeypatch):
    class MockImportJSONToCallable:
        def __init__(self, json_data_to_import, callable_write, callable_read):
            for good_value in ["a_header"]:
                # Ignore sqlite3.OperationalError because these are probably not table names that actually exist
                try:
                    callable_write(good_value, [[good_value, ""], [good_value, ""]])
                except sqlite3.OperationalError:
                    pass
                try:
                    callable_read(good_value)
                except sqlite3.OperationalError:
                    pass
            for bad_value in ["a space", 'a"quote']:
                with pytest.raises(ValueError):
                    callable_write(
                        bad_value, [["a_header", ""], ["another_header", ""]]
                    )
                with pytest.raises(ValueError):
                    callable_write(
                        "table_name", [[bad_value, ""], ["another_header", ""]]
                    )
                with pytest.raises(ValueError):
                    callable_write("table_name", [["a_header", ""], [bad_value, ""]])
                with pytest.raises(ValueError):
                    callable_read(bad_value)

        def go(self):
            pass

    monkeypatch.setattr(
        libcoveofds.gpkg.from_json, "ImportJSONToCallable", MockImportJSONToCallable
    )

    # Get new SQLite filename
    sqlite_filename = tempfile.mkstemp(suffix=".sqlite")
    os.close(sqlite_filename[0])
    sqlite_filename = sqlite_filename[1]
    # Copy template
    shutil.copyfile(
        os.path.join(
            "libcoveofds",
            "data",
            "schema_0_4",
            "network-schema.gpkg",
        ),
        sqlite_filename,
    )

    libcoveofds.gpkg.from_json.import_json_to_sqlite({}, sqlite_filename)
