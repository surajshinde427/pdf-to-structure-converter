import tabula
import pandas as pd

def extract_tables(pdf_path):
    """Extract tables from PDF using tabula-py"""
    try:
        # Extract all tables from all pages
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

        if not tables or (isinstance(tables, list) and len(tables) == 0):
            return []

        # Filter out empty dataframes
        valid_tables = []
        for table in tables:
            if isinstance(table, pd.DataFrame) and not table.empty:
                valid_tables.append(table)

        return valid_tables
    except Exception as e:
        print(f"Warning: Could not extract tables: {e}")
        return []

def tables_to_dict(tables):
    """Convert tables to dictionary format"""
    result = []
    for i, table in enumerate(tables):
        if isinstance(table, pd.DataFrame):
            result.append({
                "table_number": i + 1,
                "rows": len(table),
                "columns": len(table.columns),
                "data": table.to_dict(orient='records')
            })
    return result
