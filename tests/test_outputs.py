import json
import pytest
from pathlib import Path

@pytest.fixture
def report():
    """Loads the report file for testing."""
    path = Path("/app/report.json")
    assert path.exists(), "report.json does not exist"
    with open(path, "r") as f:
        return json.load(f)

def test_total_requests(report):
    """Verifies how many requests there were."""
    assert "total_requests" in report
    assert isinstance(report["total_requests"], int)

def test_clients_involved(report):
    """Verifies the clients involved."""
    assert "unique_ips" in report
    assert isinstance(report["unique_ips"], int)

def test_popular_pages(report):
    """Verifies which pages were popular."""
    assert "top_path" in report
    assert isinstance(report["top_path"], str)