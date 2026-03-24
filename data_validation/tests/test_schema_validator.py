"""Tests for schema_validator.py using sample fixtures."""
import pytest, json, os

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")

def test_valid_vulnerability():
    """A correctly formatted vulnerability entry should pass validation."""
    # TODO: Implement when schema_validator.validate_file() is built
    filepath = os.path.join(FIXTURES_DIR, "valid_vulnerability.json")
    assert os.path.exists(filepath), "Fixture file missing"

def test_invalid_vulnerability():
    """An entry with missing required fields should fail validation."""
    # TODO: Implement when schema_validator.validate_file() is built
    filepath = os.path.join(FIXTURES_DIR, "invalid_vulnerability.json")
    assert os.path.exists(filepath), "Fixture file missing"
