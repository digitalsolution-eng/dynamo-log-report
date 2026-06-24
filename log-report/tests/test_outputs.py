import json
from pathlib import Path

import pytest

REPORT = Path("/app/report.json")


@pytest.fixture(scope="module")
def report():
    # Criterion 1: report exists and is a single valid JSON object.
    assert REPORT.exists(), "no /app/report.json found"
    with REPORT.open() as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json is not a JSON object"
    return data


def test_report_is_valid_json_object(report):
    # Criterion 1: /app/report.json exists and is a single valid JSON object.
    assert set(report.keys()) >= {"total_requests", "unique_ips", "top_path"}


def test_total_requests(report):
    # Criterion 2: total_requests equals the number of request lines (6).
    assert report["total_requests"] == 6


def test_unique_ips(report):
    # Criterion 3: unique_ips equals the number of distinct client IPs (3).
    assert report["unique_ips"] == 3


def test_top_path(report):
    # Criterion 4: top_path equals the most-requested path (/index.html, 3 hits).
    assert report["top_path"] == "/index.html"
