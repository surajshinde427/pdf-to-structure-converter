import pytest
import json
from pdfextract.formatters import format_json

def test_format_json_simple_dict():
    """Test JSON formatting with simple dictionary"""
    data = {"text": "Sample text", "pages": 5}
    result = format_json(data)
    parsed = json.loads(result)
    assert parsed == data

def test_format_json_empty_dict():
    """Test JSON formatting with empty dictionary"""
    data = {}
    result = format_json(data)
    parsed = json.loads(result)
    assert parsed == {}
