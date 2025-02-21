# Excel Data Cleaning Scripts

A collection of simple Python scripts for cleaning Excel data, designed for college students learning data cleaning techniques.

## Scripts Overview

1. `create_data.py`
   - Creates a sample Excel file with common data issues
   - Includes missing values, duplicates, and formatting inconsistencies
   - Generates 'student_data.xlsx'

2. `remove_missing.py`
   - Removes rows with missing values
   - Creates 'student_data_clean.xlsx'

3. `remove_duplicate.py`
   - Removes exact duplicate rows
   - Creates 'student_data_no_duplicates.xlsx'

4. `standardize_format.py`
   - Standardizes text case
   - Removes extra spaces
   - Fixes typos
   - Creates 'student_data_standardized.xlsx'

## Setup and Installation

1. Make sure you have Python 3.6 or higher installed
2. Install Repo
   ```bash
   git clone https://github.com/ronantakizawa/pythonexceldatacleaning.git
   cd pythonexceldatacleanin
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Data Issues Covered

- Missing values
- Duplicate records
- Inconsistent text formatting
- Extra spaces
- Typos

## File Outputs

- `student_data.xlsx` - Original data with issues
- `student_data_clean.xlsx` - Data with missing values removed
- `student_data_no_duplicates.xlsx` - Data with duplicates removed
- `student_data_standardized.xlsx` - Data with standardized formatting

## Dependencies
See requirements.txt for the complete list of dependencies. Main packages used:
- pandas
- numpy