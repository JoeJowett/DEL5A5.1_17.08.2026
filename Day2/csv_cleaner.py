import pandas as pd
import time
from pathlib import Path
from datetime import datetime


# -----------------------------------
# Setup
# -----------------------------------

start_time = time.time()

DATA_DIR = Path(__file__).resolve().parent / "Data"
DATA_DIR.mkdir(exist_ok=True)

customers_file = DATA_DIR / "03_Library SystemCustomers.csv"
books_file = DATA_DIR / "03_Library Systembook.csv"

customers_clean_file = DATA_DIR / "03_Library SystemCustomers_clean.csv"
books_clean_file = DATA_DIR / "03_Library Systembook_cleaner.csv"

metrics_file = DATA_DIR / "data_engineering_metrics.csv"


# -----------------------------------
# Load source data
# -----------------------------------

customers_raw = pd.read_csv(customers_file)
books_raw = pd.read_csv(books_file)

print("Source data loaded successfully.")


# -----------------------------------
# Create metrics
# -----------------------------------

metrics = []

run_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_metric(dataset, metric, value):
    metrics.append({
        "Run Timestamp": run_timestamp,
        "Dataset": dataset,
        "Metric": metric,
        "Value": value
    })


# -----------------------------------
# Customer metrics
# -----------------------------------

customer_source_rows = len(customers_raw)

add_metric(
    "Customers",
    "Source Rows",
    customer_source_rows
)

customer_missing = customers_raw.isna().sum().sum()

add_metric(
    "Customers",
    "Missing Values",
    customer_missing
)

customer_duplicates = customers_raw.duplicated().sum()

add_metric(
    "Customers",
    "Duplicate Rows",
    customer_duplicates
)


# Clean customers
customers = customers_raw.dropna()

customer_clean_rows = len(customers)

add_metric(
    "Customers",
    "Clean Rows",
    customer_clean_rows
)

add_metric(
    "Customers",
    "Rows Removed",
    customer_source_rows - customer_clean_rows
)


# -----------------------------------
# Book metrics
# -----------------------------------

book_source_rows = len(books_raw)

add_metric(
    "Books",
    "Source Rows",
    book_source_rows
)

book_missing = books_raw.isna().sum().sum()

add_metric(
    "Books",
    "Missing Values",
    book_missing
)

book_duplicates = books_raw.duplicated().sum()

add_metric(
    "Books",
    "Duplicate Rows",
    book_duplicates
)


# -----------------------------------
# Clean books
# -----------------------------------

books = books_raw.dropna()

# Rename column
books = books.rename(
    columns={'Book checkout': 'Book Checkout'}
)


# -----------------------------------
# Convert dates
# -----------------------------------

books['Book Checkout'] = pd.to_datetime(
    books['Book Checkout'].str.strip('"'),
    dayfirst=True,
    errors='coerce'
)

books['Book Returned'] = pd.to_datetime(
    books['Book Returned'].str.strip('"'),
    dayfirst=True,
    errors='coerce'
)


# Track invalid dates
invalid_checkout_dates = books['Book Checkout'].isna().sum()
invalid_return_dates = books['Book Returned'].isna().sum()

add_metric(
    "Books",
    "Invalid Checkout Dates",
    invalid_checkout_dates
)

add_metric(
    "Books",
    "Invalid Return Dates",
    invalid_return_dates
)

# Remove rows with invalid dates
books = books.dropna(
    subset=['Book Checkout', 'Book Returned']
)


# -----------------------------------
# Convert borrowing period
# -----------------------------------

books['Days allowed to borrow'] = (
    books['Days allowed to borrow']
    .astype(str)
    .str.extract(r'(\d+(?:\.\d+)?)')[0]
)

books['Days allowed to borrow'] = pd.to_numeric(
    books['Days allowed to borrow'],
    errors='coerce'
) * 7


# -----------------------------------
# Calculate days borrowed
# -----------------------------------

books['Days Borrowed'] = (
    books['Book Returned'] -
    books['Book Checkout']
).dt.days


# -----------------------------------
# Overdue calculation
# -----------------------------------

books['Overdue'] = books['Days Borrowed'].apply(
    lambda x: 'Overdue' if x > 14 else 'On time'
)


overdue_count = (
    books['Overdue'] == 'Overdue'
).sum()

on_time_count = (
    books['Overdue'] == 'On time'
).sum()


add_metric(
    "Books",
    "Overdue Books",
    overdue_count
)

add_metric(
    "Books",
    "On Time Books",
    on_time_count
)


# -----------------------------------
# Clean book row count
# -----------------------------------

book_clean_rows = len(books)

add_metric(
    "Books",
    "Clean Rows",
    book_clean_rows
)

add_metric(
    "Books",
    "Rows Removed",
    book_source_rows - book_clean_rows
)


# -----------------------------------
# Save cleaned data
# -----------------------------------

customers.to_csv(
    customers_clean_file,
    index=False
)

books.to_csv(
    books_clean_file,
    index=False
)


# -----------------------------------
# Pipeline metrics
# -----------------------------------

processing_time = round(
    time.time() - start_time,
    2
)

add_metric(
    "Pipeline",
    "Processing Time Seconds",
    processing_time
)

add_metric(
    "Pipeline",
    "Status",
    "Success"
)


# -----------------------------------
# Save metrics
# -----------------------------------

metrics_df = pd.DataFrame(metrics)

metrics_df.to_csv(
    metrics_file,
    index=False
)


# -----------------------------------
# Output results
# -----------------------------------

print("\n==============================")
print("DATA ENGINEERING METRICS")
print("==============================")

print(metrics_df.to_string(index=False))


print("\n==============================")
print("CLEANED CUSTOMERS")
print("==============================")

print(customers.to_string(index=False))


print("\n==============================")
print("CLEANED BOOKS")
print("==============================")

print(books.to_string(index=False))


print("\n==============================")
print("PIPELINE COMPLETE")
print("==============================")

print(f"Metrics saved to: {metrics_file}")
print(f"Processing time: {processing_time} seconds")
