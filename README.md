# Freebie Tracker

## Project Overview

The Freebie Tracker is a Python-based application that helps developers track freebies they receive from different companies at hackathons and events. It uses SQLAlchemy for ORM (Object Relational Mapping) and Alembic for database migrations.

## Technologies Used

Python 3.8+

SQLite (Database)

SQLAlchemy (ORM)

Alembic (Migrations)

IPDB (Debugging)

## Project Structure

.
├── lib
│   ├── models.py        # SQLAlchemy models for Company, Dev, and Freebie
│   ├── seed.py          # Script to populate the database with sample data
│   ├── debug.py         # Interactive debugging tool using IPDB
│   ├── config.py        # Database configuration
├── migrations           # Alembic migration scripts
├── README.md            # Project documentation (this file)
└── Pipfile              # Dependency management

## Database Schema

The project consists of three models:

Company (has many freebies)

Dev (has many freebies)

Freebie (belongs to a Dev and a Company)

## Relationships:

A Company can give multiple Freebies to developers.

A Dev can collect multiple Freebies from different companies.

A Freebie is associated with one Company and one Dev.

## Setup & Installation

1️. Install Dependencies

pipenv install

2️. Activate Virtual Environment

pipenv shell

3️. Run Database Migrations

alembic upgrade head

4️. Seed the Database

python seed.py

5️. Run Debugging Tool

python debug.py

## Usage

Inside debug.py, you can test queries interactively:

from models import session, Company, Dev, Freebie

# Fetch all companies
devs = session.query(Dev).all()
print(devs)

✅ Features

Track freebies given to developers.

Add new freebies to the database.

Query developers and the companies they received freebies from.

🔍 Testing Your Code

You can use the IPDB debugger inside debug.py:

ipdb.set_trace()

Run queries to check if everything is working as expected.

## Troubleshooting

Missing alembic.ini error? Ensure you’re in the correct directory where alembic.ini is located.

Empty database after seeding? Run python seed.py again and check with session.query(Company).all().

IPDB not found? Install it inside the virtual environment:

pip install ipdb

👨‍💻 Contributors

Elias Bosire - Developer

📜 License

This project is licensed under the MIT License.