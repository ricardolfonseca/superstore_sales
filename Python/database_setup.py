from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, Date, Numeric
import pandas as pd

def load_to_postgres(cleaned_data_path):
    # Use the correct PostgreSQL credentials
    engine = create_engine('postgresql://postgres:password@localhost:5432/superstore_sales')
    
    # Load cleaned data
    df = pd.read_csv(cleaned_data_path)
    
    # Standardize column names to lowercase with underscores
    df.columns = [
        "row_id", "order_id", "order_date", "ship_date", "ship_mode",
        "customer_id", "customer_name", "segment", "country", "city",
        "state", "postal_code", "region", "product_id", "category",
        "sub_category", "product_name", "sales"
    ]
    
    # Define SQLAlchemy data types
    dtype_map = {
        "row_id": Integer,
        "order_id": Text,
        "order_date": Date,
        "ship_date": Date,
        "ship_mode": Text,
        "customer_id": Text,
        "customer_name": Text,
        "segment": Text,
        "country": Text,
        "city": Text,
        "state": Text,
        "postal_code": Integer,
        "region": Text,
        "product_id": Text,
        "category": Text,
        "sub_category": Text,
        "product_name": Text,
        "sales": Numeric
    }
    
    # Load data into the PostgreSQL table with specified data types
    df.to_sql(
        name="sales_data",
        con=engine,
        if_exists="replace",
        index=False,
        dtype=dtype_map
    )
    print("Data successfully loaded into PostgreSQL with correct data types!")
