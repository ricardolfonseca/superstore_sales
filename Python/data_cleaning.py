import pandas as pd

def clean_data(input_file, output_file):
    # Load data and parse date columns
    df = pd.read_csv(
        input_file,
        parse_dates=['Order Date', 'Ship Date'],
        dayfirst=True
    )
    
    # Handle missing values
    df['Postal Code'] = df['Postal Code'].fillna(0)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Save the cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
