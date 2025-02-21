import pandas as pd

def remove_duplicates(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Show original data info
    print("Original Data Shape:", df.shape)
    print("\nNumber of exact duplicate rows:", len(df[df.duplicated()]))
    
    # Remove exact duplicates
    df_no_duplicates = df.drop_duplicates()
    
    # Show results
    print("\nShape after removing duplicates:")
    print(df_no_duplicates.shape)
    
    # Save cleaned data
    df_no_duplicates.to_excel('student_data_no_duplicates.xlsx', index=False)
    print("\nCleaned data saved to 'student_data_no_duplicates.xlsx'")

# Direct execution
remove_duplicates('student_data.xlsx')
