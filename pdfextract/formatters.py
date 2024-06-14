import json
import csv
import pandas as pd

def format_json(data):
    """Format data as JSON"""
    # Handle pandas DataFrames
    if isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, pd.DataFrame):
                result.append(item.to_dict(orient='records'))
            else:
                result.append(item)
        return json.dumps(result, indent=2, default=str)
    return json.dumps(data, indent=2, default=str)

def format_csv(tables):
    """Format tables as CSV - handles multiple tables"""
    if not tables:
        return ""

    output = []

    # Handle list of table dictionaries (from tables_to_dict)
    if isinstance(tables, list) and len(tables) > 0:
        if isinstance(tables[0], dict) and 'data' in tables[0]:
            # Format from tables_to_dict output
            for table_info in tables:
                output.append(f"# Table {table_info['table_number']}")
                data = table_info['data']
                if data:
                    # Write header
                    headers = list(data[0].keys())
                    output.append(",".join(headers))
                    # Write rows
                    for row in data:
                        output.append(",".join(str(row.get(h, '')) for h in headers))
                output.append("")  # Blank line between tables
        else:
            # Fallback for raw dataframes
            for i, table in enumerate(tables):
                if isinstance(table, pd.DataFrame):
                    output.append(f"# Table {i+1}")
                    output.append(table.to_csv(index=False))
                    output.append("")

    return "\n".join(output)

def save_output(data, filepath, format="json"):
    """Save data to file"""
    with open(filepath, 'w') as f:
        if format == "json":
            f.write(format_json(data))
        elif format == "csv":
            f.write(format_csv(data))
        else:
            f.write(str(data))
