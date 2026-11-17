# Sales Analytics API

A lightweight REST API for exploring sales data stored in PostgreSQL. Built with **Python**, **FastAPI**, and **psycopg**.

## Features

- View sales records
- Retrieve total revenue, number of sales, and unique customer count
- Calculate average order value
- Explore category-level sales metrics
- Retrieve the latest sale
- Browse sales with pagination

## Tech Stack

- **Python** — application logic
- **FastAPI** — REST API
- **PostgreSQL** — relational database
- **psycopg 3** — database connectivity
- **python-dotenv** — environment variables
- **uv** — dependency management

## Getting Started

### Prerequisites

- Python
- PostgreSQL database containing an `orders` table
- [uv](https://docs.astral.sh/uv/)

### Installation

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Install the dependencies:

```bash
uv sync
```

Create a `.env` file in the project root:

```dotenv
DB_URL=postgresql://username:password@host:5432/database_name
```

> Never commit your `.env` file or database credentials. Add `.env` to `.gitignore`.

Start the API (assuming `main.py` contains the FastAPI `app`):

```bash
uv run uvicorn main:app --reload
```

Open the interactive API documentation at **http://127.0.0.1:8000/docs**.

## API Endpoints

The following endpoints are implemented in the FastAPI application:

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/home` | Basic health check |
| GET | `/db` | Retrieve all sales records |
| GET | `/total_revenue` | Total sales revenue |
| GET | `/number_of_customer` | Number of unique customers |
| GET | `/number_of_sales` | Total number of sales |

The query layer also includes functions for average order value, category metrics, latest sale, and paginated sales. Expose these as API routes if they are not already registered in `main.py`.

## Database

The application expects an `orders` table with columns similar to:

| Column | Type |
| --- | --- |
| `order_id` | INTEGER (primary key) |
| `order_date` | DATE |
| `customer_id` | INTEGER |
| `product_id` | INTEGER |
| `product_name` | TEXT |
| `category` | TEXT |
| `quantity` | INTEGER |
| `unit_price` | NUMERIC(12,2) |
| `total_amount` | NUMERIC(12,2) |

The schema above describes the expected data; this repository does not automatically create or populate the database.

## Project Structure

```text
.
├── main.py          # FastAPI routes
├── queries.py       # PostgreSQL queries
├── pyproject.toml    # Project dependencies
├── uv.lock           # Locked dependencies
├── .env              # Local credentials (not committed)
└── README.md
```

## Project Goal

This project is a first hands-on exercise in connecting a Python backend to a relational database, writing SQL analytics queries, and exposing results through a REST API.

## License

No license has been specified yet.
