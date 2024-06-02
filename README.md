# PDF Extract Pro

Extract structured data from PDFs - tables, text, and metadata into JSON or CSV.

## Why I Built This

Tired of manually copying tables from PDF reports. Built this to automate extracting data from messy PDFs.

## Features

- Extract text from PDFs
- Detect and extract tables automatically
- Export to JSON, CSV, or plain text
- Command line tool + Python API
- Get PDF metadata (author, dates, etc.)

## Installation

Requires Java for table extraction (tabula-py dependency).

```bash
pip install -r requirements.txt
pip install -e .
```

## Quick Start

```bash
# Extract everything
pdfextract document.pdf

# Get JSON output
pdfextract document.pdf --format json -o output.json

# Tables only
pdfextract document.pdf --tables-only

# Include metadata
pdfextract document.pdf --metadata
```

## Python API

```python
from pdfextract import extract_text
from pdfextract.tables import extract_tables
from pdfextract.metadata import extract_metadata

# Extract text
text = extract_text("document.pdf")

# Extract tables
tables = extract_tables("document.pdf")

# Get metadata
metadata = extract_metadata("document.pdf")
```

## Use Cases

- Extract financial data from statements
- Parse invoices and receipts
- Get tables from research papers
- Convert PDF reports to structured data

## Development

```bash
git clone https://github.com/surajshinde/pdf-extract-pro.git
cd pdf-extract-pro
pip install -e .[dev]
pytest tests/
```

## Requirements

- Python >= 3.8
- Java (for table extraction)

## Dependencies

- pypdf - PDF text extraction
- tabula-py - Table extraction
- pandas - Data handling

## Todo

- [ ] OCR support for scanned PDFs
- [ ] Better table detection
- [ ] Excel output
- [ ] Batch processing
- [ ] Password-protected PDFs
