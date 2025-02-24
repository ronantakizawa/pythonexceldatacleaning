import pandas as pd

def standardize_format(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    # 1. Standardize text case
    df['Name'] = df['Name'].str.title()  # Capitalize first letter of each word
    
    # 2. Remove leading/trailing whitespace
    df['Major'] = df['Major'].str.strip()
    
    # 3. Fix common typos in Major
    typo_corrections = {
        'Computter Science': 'Computer Science'
    }
    df['Major'] = df['Major'].replace(typo_corrections)
    
    # 4. Standardize date format
    df['Enrollment Date'] = pd.to_datetime(df['Enrollment Date']).dt.strftime('%Y-%m-%d')
    
    # Save processed dataset
    df.to_excel('student_data_standardized.xlsx', index=False)

standardize_format('student_data.xlsx')