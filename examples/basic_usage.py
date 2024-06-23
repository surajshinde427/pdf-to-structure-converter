#!/usr/bin/env python3
"""
Basic usage example for pdf-extract-pro
"""

import sys
from pdfextract import extract_text
from pdfextract.tables import extract_tables
from pdfextract.metadata import extract_metadata

def main():
    if len(sys.argv) < 2:
        print("Usage: python basic_usage.py <pdf_file>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    print(f"Processing: {pdf_file}\n")

    # Extract text
    text = extract_text(pdf_file)
    print("=== TEXT ===")
    print(text[:500])  # First 500 chars

    # Extract tables
    tables = extract_tables(pdf_file)
    print(f"\n=== TABLES ({len(tables)} found) ===")
    for i, table in enumerate(tables):
        print(f"\nTable {i+1}:")
        print(table.head())

    # Extract metadata
    metadata = extract_metadata(pdf_file)
    print("\n=== METADATA ===")
    for key, value in metadata.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
