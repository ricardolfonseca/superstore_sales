from data_cleaning import clean_data
from database_setup import load_to_postgres


if __name__ == '__main__':
    
    # Step 1: Data Cleaning
    cleaned_data_path = "cleaned_sales_data.csv"
    clean_data("dataset.csv", cleaned_data_path)

    # Step 2: Load into PostgreSQL
    load_to_postgres(cleaned_data_path)

    print("Workflow completed successfully!")
