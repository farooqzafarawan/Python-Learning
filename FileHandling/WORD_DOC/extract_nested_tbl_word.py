from docx import Document
import pandas as pd
from typing import List, Dict, Any

def extract_nested_tables(docx_path: str) -> List[pd.DataFrame]:
    """
    Extract nested tables from a Word document efficiently without redundant cell access.
    
    Args:
        docx_path (str): Path to the Word document
        
    Returns:
        List[pd.DataFrame]: List of DataFrames containing the table data
    """
    doc = Document(docx_path)
    all_tables = []
    
    def extract_cell_text(cell) -> str:
        """Extract text from a cell, handling nested tables."""
        # If cell has no tables, return its text
        if not cell._element.xpath('.//w:tbl'):
            return cell.text.strip()
        # If cell has tables, return empty string (tables will be processed separately)
        return ''
    
    def process_table(table) -> Dict[str, Any]:
        """Process a single table and return its data."""
        data = []
        headers = []
        
        # Extract headers from the first row
        for cell in table.rows[0].cells:
            headers.append(extract_cell_text(cell))
        
        # Extract data from remaining rows
        for row in table.rows[1:]:
            row_data = []
            for cell in row.cells:
                # Process main cell content
                cell_text = extract_cell_text(cell)
                row_data.append(cell_text)
                
                # Check for nested tables
                nested_tables = cell._element.xpath('.//w:tbl')
                if nested_tables:
                    for nested_table in nested_tables:
                        # Convert nested_table element to Table object
                        table_obj = table.__class__(nested_table, table._parent)
                        nested_data = process_table(table_obj)
                        if nested_data['data']:  # Only add if there's actual data
                            nested_df = pd.DataFrame(nested_data['data'], 
                                                   columns=nested_data['headers'])
                            all_tables.append(nested_df)
            
            data.append(row_data)
        
        return {'headers': headers, 'data': data}
    
    # Process main tables
    for table in doc.tables:
        table_data = process_table(table)
        main_df = pd.DataFrame(table_data['data'], columns=table_data['headers'])
        all_tables.append(main_df)
    
    return all_tables

def save_tables_to_excel(tables: List[pd.DataFrame], output_path: str):
    """
    Save extracted tables to separate sheets in an Excel file.
    
    Args:
        tables (List[pd.DataFrame]): List of DataFrames to save
        output_path (str): Path for the output Excel file
    """
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        for i, df in enumerate(tables):
            sheet_name = f'Table_{i+1}'
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Example usage
if __name__ == "__main__":
    # Example usage of the functions
    docx_path = "sample.docx"
    output_path = "extracted_tables.xlsx"
    
    try:
        # Extract all tables
        tables = extract_nested_tables(docx_path)
        
        # Print summary of extracted tables
        print(f"Successfully extracted {len(tables)} tables")
        for i, df in enumerate(tables):
            print(f"\nTable {i+1} Shape: {df.shape}")
            print(f"Table {i+1} Columns: {df.columns.tolist()}")
        
        # Save to Excel
        save_tables_to_excel(tables, output_path)
        print(f"\nTables saved to {output_path}")
        
    except Exception as e:
        print(f"Error processing document: {str(e)}")