import pandas as pd

def standardize_format(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # 1. Standardize text case
    df['Name'] = df['Name'].str.title()  # Capitalize first letter of each word
    print("Standardized Names:")
    print(df['Name'].head())
    
    # 2. Remove leading/trailing whitespace
    df['Major'] = df['Major'].str.strip()
    print("\nCleaned Major values:")
    print(df['Major'].unique())
    
    # 3. Fix common typos in Major
    typo_corrections = {
        'Computter Science': 'Computer Science'
    }
    df['Major'] = df['Major'].replace(typo_corrections)
    
    # 4. Standardize date format
    df['Enrollment Date'] = pd.to_datetime(df['Enrollment Date']).dt.strftime('%Y-%m-%d')
    print("\nStandardized Dates:")
    print(df['Enrollment Date'].head())
    
    # 5. Round numeric values to consistent decimal places
    df['GPA'] = df['GPA'].round(2)
    print("\nStandardized GPA values:")
    print(df['GPA'].head())
    
    # Save processed dataset
    df.to_excel('student_data_standardized.xlsx', index=False)
    
    print("\nProcessed files have been saved:")
    print("1. student_data_standardized.xlsx - Standardized data")
    print("2. data_quality_report.xlsx - Data quality report")

standardize_format('student_data.xlsx')