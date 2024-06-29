import psycopg2
import psycopg2.extras

# Database configuration
DB_NAME = "postgres"
DB_USER = "yassien"
DB_PASS = "yassien1234"
DB_HOST = "localhost"
DB_PORT = "5432"

# Establish the connection
database_session = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

# Create a cursor
cursor = database_session.cursor(cursor_factory=psycopg2.extras.DictCursor)
