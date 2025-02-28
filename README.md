# Student Application

A simple web application for collecting and storing student information using Flask and PostgreSQL.

## Overview

This application provides a web form to collect student information (name and email) and stores it in a PostgreSQL database. It uses:
- Flask for the backend server
- SQLAlchemy for database operations
- JavaScript for asynchronous form submission
- HTML/CSS for the user interface

## Prerequisites

- Python 3.7+
- PostgreSQL database server
- pip (Python package manager)

## Installation

1. Clone this repository or download the source code:
   ```
   git clone <repository-url>
   cd student_app
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install flask sqlalchemy psycopg2
   ```

## Database Setup

1. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE student_app_db;
   ```

2. Set up your database credentials in `app.py` or use environment variables:
   ```python
   DB_HOST = "localhost"
   DB_NAME = "student_app_db"
   DB_USER = "postgres"
   DB_PASSWORD = "postgres"
   DB_PORT = "5432"
   ```

## Running the Application

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
student_app/
│
├── app.py                 # Flask application and database models
│
├── static/
│   └── script.js          # JavaScript for form handling
│   └── style.css          # CSS styling
│
└── templates/
    └── index.html         # HTML form template
```
## Usage

1. Fill out the student information form with name (required) and email (optional).
2. Submit the form.
3. The data will be stored in the PostgreSQL database.
4. Success or error messages will be displayed on the form page.
