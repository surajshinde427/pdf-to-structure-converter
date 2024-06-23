import pytest
import os
from pdfextract.extractor import extract_text

def test_extract_text_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file"""
    with pytest.raises(FileNotFoundError):
        extract_text("nonexistent.pdf")

def test_extract_text_invalid_extension():
    """Test that ValueError is raised for non-PDF file"""
    with pytest.raises(ValueError):
        extract_text("test.txt")
