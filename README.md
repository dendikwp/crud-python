# Flask CRUD Application

This repository contains a simple CRUD (Create, Read, Update, Delete) application built using the Flask framework. It serves as a basic example of how to perform CRUD operations with Python and Flask.

---

## Features

- Create new records.
- Read and display records.
- Update existing records.
- Delete records.

## Requirements

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or newer
- pip (Python package manager)

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-crud-app.git
    cd flask-crud-app
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

1. Update the `config.py` file with your database configuration or other project settings.

2. Initialize the database:
    ```bash
    flask db upgrade
    ```

---

## Usage

1. Run the application:
    ```bash
    flask run
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

---
