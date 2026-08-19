import pandas as pd

customers = pd.read_csv(
    "/data/Data/03_Library SystemCustomers_clean.csv"
)

books = pd.read_csv(
    "/data/Data/03_Library Systembook_cleaner.csv"
)

print("\n=== CUSTOMERS ===")
print(customers)

print("\n=== BOOKS ===")
print(books)