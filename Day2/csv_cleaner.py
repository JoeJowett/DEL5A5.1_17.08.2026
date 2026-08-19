import pandas as pd

# Import customers CSV
customers = pd.read_csv("Data/03_Library SystemCustomers.csv")

# Import books CSV
books = pd.read_csv("Data/03_Library Systembook.csv")


# Check for duplicates
def check_duplicates(books):
    duplicates = books[books.duplicated()]

    if duplicates.empty:
        print("No duplicates found.")
    else:
        print("Duplicates found:")
        print(duplicates)

    return duplicates


# -------------------------
# Clean customers
# -------------------------

customers = customers.dropna()

# Export clean version
customers.to_csv(
    "Data/03_Library SystemCustomers_clean.csv",
    index=False
)


# -------------------------
# Clean books
# -------------------------

books = books.dropna()

# Rename column
books = books.rename(
    columns={'Book checkout': 'Book Checkout'}
)

# Remove quotations and convert to datetime
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

# Convert allowed borrowing period from weeks to days
books['Days allowed to borrow'] = (
    books['Days allowed to borrow']
    .astype(str)
    .str.extract(r'(\d+(?:\.\d+)?)')[0]
)

books['Days allowed to borrow'] = pd.to_numeric(
    books['Days allowed to borrow'],
    errors='coerce'
) * 7


# Calculate difference between checkout and return
def calculate_days_difference(row):
    return (row['Book Returned'] - row['Book Checkout']).days


books['Days Borrowed'] = books.apply(
    calculate_days_difference,
    axis=1
)


# Flag overdue books
books['Overdue'] = books['Days Borrowed'].apply(
    lambda x: 'Overdue' if x > 14 else 'On time'
)


# Export clean version
books.to_csv(
    "Data/03_Library Systembook_cleaner.csv",
    index=False
)


# -------------------------
# Output cleaned DataFrames
# -------------------------

print("\n==============================")
print("CLEANED CUSTOMERS")
print("==============================")
print(customers.to_string(index=False))

print("\n==============================")
print("CLEANED BOOKS")
print("==============================")
print(books.to_string(index=False))
