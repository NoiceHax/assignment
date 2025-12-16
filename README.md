📊 Data Engineering Assignment — End-to-End ETL & Optimization
Overview

This project implements an end-to-end data engineering workflow using real public datasets.
It demonstrates how raw data is extracted, cleaned, validated, stored in a relational database, queried efficiently, and supported by automation at the data source.

The focus of this project is practical execution, handling real-world data issues, and validating results through queries and performance benchmarks.

Project Objectives

Build a complete ETL (Extract–Transform–Load) pipeline

Work with both clean and messy public datasets

Design a normalized relational database schema

Validate and clean data before ingestion

Optimize SQL queries using indexes and views

Automate source-level validation using Google Apps Script

Document and verify all steps with logs and screenshots

Datasets Used
1️⃣ Clean Dataset

University Dataset (CSV)

Structured and consistent data

Used to represent clean reference data

Minimal transformation required

2️⃣ Messy Dataset

NYC Restaurant Inspection Results (CSV)

Real-world dataset with missing values and inconsistencies

Required extensive cleaning and validation

Used to demonstrate real ETL challenges

To enable faster iteration, both datasets were trimmed to representative subsets while preserving their original structure.

Database Design

The database follows a normalized relational schema to ensure data integrity and efficient querying.

Core Tables

universities

Stores clean reference data

restaurants

Stores restaurant information

inspections

Stores inspection-level details linked to restaurants

Design Principles

Primary keys uniquely identify records

Foreign keys enforce relationships

Redundancy is minimized

Schema supports analytical queries and joins

ETL Pipeline

The ETL pipeline is implemented in Python and follows a modular structure.

Extract

Data is read from public CSV files using pandas

Transform

Missing and invalid values are handled

Numeric ranges are validated

Inconsistent text fields are cleaned

Messy data is normalized

Invalid records are filtered out

Load

Cleaned data is inserted into PostgreSQL (NeonDB)

Data is loaded in batches

Referential integrity is preserved

ETL execution is verified using terminal logs and row-count validation queries.

SQL Queries & Optimization
Data Verification

Row count checks confirm successful ingestion

Join queries verify relational integrity

Query Optimization

Baseline query performance measured

Index created on foreign key columns

Queries re-executed after optimization

Performance compared using EXPLAIN ANALYZE

Views

Logical views created for simplified querying

Materialized views used for faster analytical queries

Refresh mechanisms demonstrated

Automation with Google Apps Script

Google Apps Script is used for source-level validation before ETL execution.

Key Features

Triggered automatically on sheet edits (onEdit)

Validates required fields and formats

Detects invalid or incomplete records

Updates record status (READY / INVALID)

Prevents bad data from entering the ETL pipeline

This automation reduces downstream failures and improves data quality.

Validation & Verification

ETL execution logs confirm successful runs

SQL queries verify data correctness

Domain checks ensure valid numeric ranges

Join queries confirm relational links

Performance benchmarks validate optimizations

All results are supported with screenshots and logs.

Project Structure
📂 Data Engineering Assignment
 ├── etl/
 │   ├── extract.py
 │   ├── transform.py
 │   ├── load.py
 │   └── run_etl.py
 ├── sql/
 │   └── schema.sql
 ├── data/
 │   └── public datasets (CSV)
 ├── logs/
 └── README.md

Technologies Used

Python (pandas, psycopg2)

PostgreSQL (NeonDB)

SQL

Google Apps Script

Notion (documentation & presentation)

Gamma (presentation slides)

Key Learnings

Real-world data is rarely clean

Early validation simplifies ETL pipelines

Proper indexing significantly improves performance

Normalized schemas simplify analytics

Automation at the source prevents costly downstream errors

Conclusion

This project demonstrates a complete, real-world data engineering workflow—from ingestion and validation to storage, optimization, and documentation.
It emphasizes practical problem solving, clean design, and verifiable results using real datasets and tools.
