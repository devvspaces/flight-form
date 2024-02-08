# Flight Form Backend

This is the backend for the flight form application. It is built using Django and Python.

## Installation

1. Clone the repository

2. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

3. Setup environment variables in a .env file in the root directory of the project. The following environment variables are required:

Copy the `.env.example` file to a `.env` file and set the environment variables.

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

If you are running the postgres database on your local machine, the DB_HOST should be `localhost`.

Postgres defaults to port 5432.

If you want to use SQLite, you can set the following environment variables:

```bash
DB_OPTION=sqlite
```

4. Run the following command to migrate the database:

```bash
python manage.py migrate
```

5. Run the following command to start the server:

```bash
python manage.py runserver
```

## Usage

The API endpoints can be accessed at the following URL:

```bash
http://localhost:8000/submit-flight/
```

Form data can be submitted to the above endpoint using a POST request.
