import pytest
from pdfextract.tables import extract_tables, tables_to_dict

def test_extract_tables_nonexistent_file():
    """Test that extract_tables handles non-existent files gracefully"""
    result = extract_tables("nonexistent.pdf")
    assert result == []

def test_tables_to_dict_empty_list():
    """Test tables_to_dict with empty list"""
    result = tables_to_dict([])
    assert result == []
