import pandas as pd
import numpy as np

def handle_missing_values(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    print("Original Data Shape:", df.shape)
    print("\nMissing Values Count:")
    print(df.isnull().sum())
    
    # 1. Remove rows with missing values
    df_dropna = df.dropna()
    print("\nShape after removing rows with missing values:")
    print(df_dropna.shape)
    
    # 2. Fill missing values with mean/mode
    df_filled = df.copy()
    # Fill numeric columns with mean
    df_filled['GPA'] = df_filled['GPA'].fillna(df_filled['GPA'].mean())
    # Fill categorical columns with mode
    df_filled['Major'] = df_filled['Major'].fillna(df_filled['Major'].mode()[0])
    
    print("\nFilled missing values:")
    print("GPA filled with mean:", df_filled['GPA'].iloc[2])  # Check previously missing value
    print("Major filled with mode:", df_filled['Major'].iloc[5])  # Check previously missing value
    
    # 3. Fill missing values with custom logic
    df_custom = df.copy()
    # Fill GPA with median if age > 20, else mean
    median_gpa = df_custom['GPA'].median()
    mean_gpa = df_custom['GPA'].mean()
    
    df_custom['GPA'] = df_custom.apply(
        lambda row: median_gpa if pd.isna(row['GPA']) and row['Age'] > 20 
        else (mean_gpa if pd.isna(row['GPA']) else row['GPA']),
        axis=1
    )
    
    # Save processed datasets
    df_filled.to_excel('student_data_filled.xlsx', index=False)
    df_custom.to_excel('student_data_custom_filled.xlsx', index=False)
    
    print("\nProcessed files have been saved:")
    print("1. student_data_filled.xlsx - Simple mean/mode imputation")
    print("2. student_data_custom_filled.xlsx - Custom imputation logic")

handle_missing_values('student_data.xlsx')