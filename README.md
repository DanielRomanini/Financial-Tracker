# Financial Tracker

## Description
A REST API that parses Wells Fargo bank transaction data from a CSV file, categorizes each transaction using keyword matching, and stores them in a SQLite database. The API exposes several endpoints to query transactions by category, date, and summary totals.

## Tech Stack
- **Python** — core language
- **Flask** — REST API framework
- **SQLite** — local database via Python's built-in `sqlite3` module
- **CSV** — transaction data parsed using Python's built-in `csv.DictReader`

## How to Run
1. Clone the repository
git clone https://github.com/yourusername/Financial-Tracker.git
2. Install Flask
pip install flask
3. Add your Wells Fargo CSV export to the project folder and name it `Checking.csv`
4. Run the tracker
python tracker.py
5. The API will be available at `http://127.0.0.1:5000`

## API Endpoints
| Endpoint | Method | Description |
|---|---|---|
| `/transactions` | GET | Returns all transactions |
| `/transactions/<type>` | GET | Returns all transactions for a specific category |
| `/transactions/<type>/total` | GET | Returns total spending for a specific category |
| `/transactions/date/<date>` | GET | Returns all transactions on a specific date (format: MM-DD-YYYY) |
| `/totals` | GET | Returns total spending for every category |
| `/summary` | GET | Returns total income, total spending, and net |

## Categories
Transactions are automatically categorized using keyword matching across 12 categories:
`groceries`, `gas`, `restaurants`, `food_delivery`, `transportation`, `subscriptions`, `entertainment`, `income`, `health_personal`, `travel`, `transfers`, `other`

## Project Structure
```
Financial-Tracker/
├── tracker.py       # Main application — CSV parsing, DB logic, Flask API
├── .gitignore       # Excludes sensitive files (CSV, database)
└── README.md        # Project documentation
```

## What I Learned
- Parsing and cleaning real-world financial data from CSV exports
- Designing a SQLite database schema and writing SQL queries
- Building a REST API with Flask and exposing data as JSON
- Connecting a database to an API and handling threading constraints
- Version control with Git and GitHub