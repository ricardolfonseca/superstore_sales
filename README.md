# Superstore Sales Analysis

This project is an end-to-end data analysis pipeline for the `Superstore Sales` dataset. The analysis involves cleaning and normalizing the data, storing it in a PostgreSQL database, performing exploratory data analysis (EDA), and generating insights. The results are presented using visualizations and structured markdown reports.

## Folder Structure


```
Superstore Sales/
├── PostgreSQL/
│   ├── Database Schema.png
│   ├── DB normalizing.ipynb
│   ├── EDA graph_monthly trend in sales over time.png
│   ├── EDA.ipynb
│   ├── Procedures, triggers and views.ipynb

├── Python/
│   ├── data_cleaning.py
│   ├── database_setup.py
│   ├── main.py
│   ├── dataset.csv
│   ├── requirements.txt
```

## How to Run the Project: Step-by-Step Instructions

1. **Save the Folder and Install Dependencies**:
   - Download or clone the entire project folder.
   - Navigate to the project directory and install the required Python libraries using:
     ```bash
     pip install -r Python/requirements.txt
     ```

2. **Run the Data Cleaning and Database Loading Script**:
   - Execute the `main.py` script in the Python folder to clean the data and load it into PostgreSQL:
     ```bash
     python Python/main.py
     ```

3. **Normalize the Database**:
   - Open **pgAdmin** (PostgreSQL) tool.
   - Execute the SQL queries in `DB normalizing.ipynb` to normalize the database into separate tables (`sales`,  `customers`, `products`, `locations`, `dim_ship_mode`).

4. **Perform Exploratory Data Analysis (EDA)**:
   - Open **pgAdmin** or your SQL editor.
   - Use the SQL queries provided in `.EDA Queries.ipynb.layout` to explore the data.
   - Alternatively, open `EDA.ipynb` for an organized query workflow in a notebook environment.

5. **Review Visualizations**:
   - Refer to `EDA graph_monthly trend in sales over time.png` for a visual representation of monthly sales trends.
   - Use tools like Power BI or Tableau to create additional visualizations, if needed.
  
6. **Enhance efficiency**:
   - Refer to `Procedures, triggers and views.ipynb` for enhancing the database with stored procedures, triggers and views.


## Project Workflow

### 1. **Data Cleaning**
The `data_cleaning.py` script:
- Reads the raw dataset from `dataset.csv`.
- Cleans and preprocesses the data, ensuring proper column naming and formats.
- Saves the cleaned data as `cleaned_sales_data.csv`.

### 2. **Database Setup**
The `main.py` script:
- Loads the cleaned data into a PostgreSQL database.
- Creates the `sales_data` table with appropriate column types.

The `DB normalizing.ipynb` notebook:
- Normalizes the database into separate tables (`sales`, `customers`, `products`, `locations`, `dim_ship_mode`).
- Ensures relationships and constraints are applied between tables.

### 3. **Exploratory Data Analysis**
The `EDA.ipynb` notebook:
- Contains SQL queries to analyze the dataset.
- Provides insights such as total sales by region, top customers, and monthly sales trends.
- Includes a visualization for sales trends generated in **pgAdmin** (`EDA graph_monthly trend in sales over time.png`).

### 4. **Database Queries**
The `.EDA Queries.ipynb.layout` file contains structured SQL queries for performing EDA, which should be run in tools like **pgAdmin** or **DBeaver**.
The `Procedures, triggers and views.ipynb` file contains structured SQL queries for creating automated processes.

## Key Findings
- **West** and **East** regions dominate sales, accounting for ~60% of total revenue.
- **Phones** and **Chairs** are the top product sub-categories.
- **Sean Miller** is the highest-spending customer.
- Sales peak during **November**, especially in **2018**.

For detailed insights, refer to the `EDA.ipynb` notebook.

## Prerequisites
- **Python**: Version 3.8 or higher
- **PostgreSQL**: Version 12 or higher
- Required Python libraries (install via `requirements.txt`):
  
    ```bash
    pip install -r requirements.txt
    ```

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For questions or suggestions, please contact the project owner at ricardolfonseca@live.com.pt.
