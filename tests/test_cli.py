import subprocess


def test_jsontogpkg(tmp_path):
    proc = subprocess.run(
        [
            "libcoveofds",
            "jsontogpkg",
            "tests/fixtures/json_to_geojson/basic_1.json",
            tmp_path / "test.gpkg",
        ]
    )
    assert proc.returncode == 0
