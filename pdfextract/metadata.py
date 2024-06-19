from pypdf import PdfReader
from datetime import datetime

def extract_metadata(pdf_path):
    """Extract metadata from PDF"""
    reader = PdfReader(pdf_path)

    metadata = {}

    # Get document info
    if reader.metadata:
        metadata['title'] = reader.metadata.get('/Title', 'N/A')
        metadata['author'] = reader.metadata.get('/Author', 'N/A')
        metadata['subject'] = reader.metadata.get('/Subject', 'N/A')
        metadata['creator'] = reader.metadata.get('/Creator', 'N/A')
        metadata['producer'] = reader.metadata.get('/Producer', 'N/A')

        # Parse dates
        created = reader.metadata.get('/CreationDate')
        if created:
            metadata['created_date'] = str(created)

        modified = reader.metadata.get('/ModDate')
        if modified:
            metadata['modified_date'] = str(modified)

    # Add page count
    metadata['pages'] = len(reader.pages)

    return metadata
