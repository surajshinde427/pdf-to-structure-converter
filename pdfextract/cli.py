#!/usr/bin/env python3
import argparse
import sys
from .extractor import extract_text
from .tables import extract_tables, tables_to_dict
from .formatters import format_json, format_csv, save_output
from .metadata import extract_metadata

def main():
    parser = argparse.ArgumentParser(description="Extract structured data from PDFs")
    parser.add_argument("pdf_file", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--format", "-f", choices=["json", "csv", "txt"],
                        default="txt", help="Output format")
    parser.add_argument("--tables-only", action="store_true",
                        help="Extract only tables")
    parser.add_argument("--text-only", action="store_true",
                        help="Extract only text")
    parser.add_argument("--metadata", "-m", action="store_true",
                        help="Include PDF metadata in output")

    args = parser.parse_args()

    result = {}

    # Extract metadata if requested
    if args.metadata:
        result['metadata'] = extract_metadata(args.pdf_file)

    # Extract text
    if not args.tables_only:
        text = extract_text(args.pdf_file)
        result['text'] = text
        if args.format == "txt":
            print("=== TEXT ===")
            print(text)

    # Extract tables
    if not args.text_only:
        tables = extract_tables(args.pdf_file)
        result['tables'] = tables_to_dict(tables)
        if args.format == "txt":
            print("\n=== TABLES ===")
            print(f"Found {len(tables)} tables")
            for i, table in enumerate(tables):
                print(f"\nTable {i+1}:")
                print(table)

    # Output handling
    if args.format == "json":
        output_text = format_json(result)
    elif args.format == "csv":
        # For CSV, only output tables
        output_text = format_csv(result.get('tables', []))
    else:
        output_text = None

    # Save to file or print to stdout
    if args.output and output_text:
        save_output(result, args.output, args.format)
        print(f"Output saved to: {args.output}")
    elif output_text:
        print(output_text)

if __name__ == "__main__":
    main()
