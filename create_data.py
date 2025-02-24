import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_sample_data():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Create sample student data
    data = {
        'Name': [
            'John Smith', 'Emma Wilson', 'Michael Brown', 'Sarah Davis', 'James Miller',
            'Lisa Garcia', 'David Lee', 'Jennifer Martinez', 'Robert Taylor', 'Maria Anderson',
            'William White', 'Linda Thomas', 'Richard Moore', 'Patricia Jackson', 'Joseph Martin',
            'Margaret Thompson', 'Charles Rodriguez', 'Sandra Lewis', 'Daniel Lee', 'Nancy Clark'
        ],
        'Age': np.random.randint(18, 25, 20),
        'GPA': np.round(np.random.uniform(2.0, 4.0, 20), 2),
        'Major': np.random.choice(
            ['Computer Science', 'Biology', 'Mathematics', 'Physics', 'Chemistry'],
            20
        ),
        'Enrollment Date': [
            (datetime(2023, 9, 1) + timedelta(days=np.random.randint(0, 30))).strftime('%Y-%m-%d')
            for _ in range(20)
        ]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add missing values
    df.loc[2, 'GPA'] = np.nan
    df.loc[5, 'Major'] = None
    
    # Add duplicate entries
    df = pd.concat([df, df.iloc[[0, 1]]])
    
    # Add inconsistent formatting
    df.loc[7, 'Name'] = 'JENNIFER MARTINEZ'
    df.loc[10, 'Name'] = 'william white'
    
    # Add leading/trailing spaces
    df.loc[3, 'Major'] = ' Biology  '
    
    # Add typo in Major
    df.loc[15, 'Major'] = 'Computter Science'
    
    # Add incorrect date format (MM/DD/YYYY instead of YYYY-MM-DD)
    df.loc[8, 'Enrollment Date'] = '09/15/2023'
    
    # Save to Excel file
    df.to_excel('student_data.xlsx', index=False)
    print("Sample student data has been created and saved to 'student_data.xlsx'")
    print("\nData issues introduced:")
    print("1. Missing values in GPA and Major columns")
    print("2. Duplicate student records")
    print("3. Inconsistent name formatting (upper/lower case)")
    print("4. Leading/trailing spaces in Major column")
    print("5. Typo in Major column ('Computter Science')")
    print("6. Incorrect date format on row 9 (09/15/2023)")
    print("7. A GPA with 3 decimal places (3.765) that needs rounding to 2 decimal places")

create_sample_data()