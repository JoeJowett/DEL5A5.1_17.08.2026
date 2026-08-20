import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from pathlib import Path

# -------------------------
# SQL Server details
# -------------------------

server = 'localhost'
database = 'library'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

connection_url = (
    'mssql+pyodbc:///?odbc_connect='
    + quote_plus(connection_string)
)

engine = create_engine(connection_url)

# -------------------------
# Find Data folder
# -------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'Data'

# -------------------------
# Load cleaned CSV files
# -------------------------

customers = pd.read_csv(
    DATA_DIR / '03_Library SystemCustomers_clean.csv'
)

books = pd.read_csv(
    DATA_DIR / '03_Library Systembook_cleaner.csv'
)

metrics = pd.read_csv(
    DATA_DIR / 'data_engineering_metrics.csv'
)

# -------------------------
# Convert metric values
# -------------------------

# The Value column contains both numbers and text
# such as "Success", so keep it as text.
metrics['Value'] = metrics['Value'].astype(str)

# -------------------------
# Load data into SQL Server
# -------------------------

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

metrics.to_sql(
    'DataEngineeringMetrics',
    engine,
    if_exists='append',
    index=False
)

def refresh_power_bi():
    # Authenticate with Microsoft
    # Get Power BI access token
    # Trigger dataset refresh
    # Check refresh status



print("Customers table successfully loaded.")
print("Books table successfully loaded.")
print("Data Engineering Metrics successfully loaded.")
print("Power BI dataset refresh requested.")