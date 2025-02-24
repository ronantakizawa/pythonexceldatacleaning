import pandas as pd

def remove_duplicates(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Remove exact duplicates
    df_no_duplicates = df.drop_duplicates()
    
    # Save cleaned data
    df_no_duplicates.to_excel('student_data.xlsx', index=False)

# Direct execution
remove_duplicates('student_data.xlsx')
