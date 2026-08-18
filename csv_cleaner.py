# import libraries
import pandas as pd

# define functions

# main code
# import customers csv
customers = pd.read_csv("Data/03_Library SystemCustomers.csv")
# drop blanks
customers = customers.dropna()
# export clean version
customers.to_csv("Data/03_Library SystemCustomers_clean.csv, index=False")

# import books csv
books = pd.read_csv("Data/03_Library Systembook.csv")
# drop blanks
books = books.dropna()
# remove quotations and convert to datetime
books['Book checkout'] = pd.to_datetime(
    books['Book checkout'].str.strip('"'),
    dayfirst=True,
    errors='coerce')
books['Book Returned'] = pd.to_datetime(
    books['Book Returned'].str.strip('"'),
    dayfirst=True,
    errors='coerce')
# convert column to days
books['Days allowed to borrow'] = (
    books['Days allowed to borrow']
    .astype(str)
    .str.extract(r'(\d+(?:\.\d+)?)')[0]
)
books['Days allowed to borrow'] = pd.to_numeric(
    books['Days allowed to borrow'],
   errors='coerce' 
) * 7
# calculate the difference between checkout and return
def calculate_days_difference(row):
    return (row['Book Returned'] - row['Book checkout']).days
books['Days Borrowed'] = books.apply(calculate_days_difference, axis=1)
# flag if overdue column
books['Overdue'] = books['Days Borrowed'].apply(
    lambda x: 'Overdue' if x > 14 else 'On time'
)
# export to csv
books.to_csv("Data/03_Library Systembook_cleaner.csv, index=False")