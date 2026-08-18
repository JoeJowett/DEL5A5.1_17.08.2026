import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from pathlib import Path

# SQL Server details
server = 'localhost'
database = 'library'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

connection_url = 'mssql+pyodbc:///?odbc_connect=' + quote_plus(connection_string)

engine = create_engine(connection_url)

# Find the Data folder relative to this Python script
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'Data'

# Load cleaned CSV files
customers = pd.read_csv(
    DATA_DIR / '03_Library SystemCustomers_clean.csv, index=False'
)

books = pd.read_csv(
    DATA_DIR / '03_Library Systembook_cleaner.csv, index=False'
)

# Add dataframes to SQL Server
customers.to_sql(
    'Customers',
    engine,
    if_exists='replace',
    index=False
)

books.to_sql(
    'Books',
    engine,
    if_exists='replace',
    index=False
)

print("Customers and Books successfully added to SQL Server")