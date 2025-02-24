import pandas as pd
import numpy as np

def handle_missing_values(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # 1. Remove rows with missing values
    df_dropna = df.dropna()
    
    # 2. Fill missing values with mean/mode
    df_filled = df.copy()
    # Fill numeric columns with mean
    df_filled['GPA'] = df_filled['GPA'].fillna(df_filled['GPA'].mean())
    # Fill categorical columns with mode
    df_filled['Major'] = df_filled['Major'].fillna(df_filled['Major'].mode()[0])
    
    # Save processed datasets
    df_filled.to_excel('student_data_missing.xlsx', index=False)

handle_missing_values('student_data.xlsx')