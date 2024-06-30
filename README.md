# Urban Field Backend

This is the backend of the Urban Field web application, a platform for booking sports venues. The backend is built with Flask and MySQL.

## Features

- User authentication and authorization
- API for managing sports venues and bookings
- Database models for users, venues, and bookings
- RESTful API endpoints

## Prerequisites

- Python (>= 3.7)
- MySQL

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/JoyAbrian/UrbanField-server.git
    cd UrbanField-server
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your environment variables:
    ```env
    FLASK_APP=run.py
    FLASK_ENV=development
    DATABASE_URI=mysql+pymysql://username:password@localhost/urban_field
    SECRET_KEY=your_secret_key
    ```

5. Set up the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Running the Application

1. Start the Flask development server:
    ```sh
    flask run
    ```

2. The API will be available at `http://localhost:5000/api`.

## Project Structure

- `app/`: Main application directory
  - `routes/`: Database models
- `sql/`: Database migration scripts

## Contributing

Feel free to submit pull requests and issues. For major changes, please open an issue first to discuss what you would like to change.
