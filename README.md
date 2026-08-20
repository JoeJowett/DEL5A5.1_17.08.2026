# DEL5A5.1_17.08.2026

# Library System Data Engineering Pipeline

## 1. Project Overview

This project implements a data engineering pipeline for a library system. Raw customer and book CSV files are cleaned using Python/ Pandas, quality and processing metrics are generated, cleaned data is loaded into SQL Server, and the resulting data is visualised in Power BI.

The objective of the solution is to create a repeatable data pipeline that:

Imports raw library customer data.
Imports raw library book data.
Cleans missing and invalid data.
Standardises column names.
Converts dates into usable date formats.
Calculates the number of days books were borrowed.
Identifies overdue books.
Tracks data quality and pipeline performance metrics.
Stores the cleaned datasets in SQL Server.
Provides data for analysis and visualisation in Power BI.

The overall pipeline is:

![Solution Architecture](Screenshots/ProposedArchitectureSolution.png)

The proposed Power BI report:

![Power BI Report](Screenshots/ProposedPowerBIReport.png)

2. Choices made and why:

Python/ Pandas – efficient for CSV processing and data cleaning.
SQL Server – provides structured relational storage and allows SQL querying.
Docker – provides a reproducible environment for running the Python pipeline.
Docker volumes – allow cleaned files to persist between containers.
Power BI – provides visualisation and reporting.
Git/GitHub – version control and project tracking.

3. Data Cleaning
What csv_cleaner.py does:

Removes missing rows.
Detects duplicates.
Renames the checkout column.
Converts dates to datetime.
Converts borrowing periods from weeks to days.
Calculates days borrowed.
Identifies overdue books.
Creates cleaned CSV files.
Generates data engineering metrics.

4. Data Engineering Metrics
I propose to track things such as:

Source row count
Clean row count
Rows removed
Missing values
Duplicate rows
Invalid dates
Overdue books
Books returned on time
Pipeline processing time
Pipeline status

5. SQL Server & Power BI

The cleaned tables and metrics are loaded into localhost SQL Server for visualising in Power BI.

6. How to Run the Pipeline

csv_cleaner.py creates the cleaned CSV files and metrics.

Then sql_loader.py loads the cleaned datasets into tables in the SQL Server

Then Power BI collects the data to provide visuals.