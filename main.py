import os
import psycopg2
import psycopg2.extras
from urllib.parse import urlparse

# Load DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set! Make sure it's available in your environment.")

# Parse DATABASE_URL
result = urlparse(DATABASE_URL)
DB_NAME = result.path[1:]  # Remove leading '/'
DB_USER = result.username
DB_PASS = result.password
DB_HOST = result.hostname
DB_PORT = result.port if result.port else 5432  # Default to 5432 if port is missing

# Ensure credentials are correctly extracted
if not all([DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT]):
    raise ValueError("❌ One or more database credentials are missing!")

# Establish the database connection
try:
    database_session = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        sslmode="require"
    )
    cursor = database_session.cursor(cursor_factory=psycopg2.extras.DictCursor)
except Exception as e:
    raise RuntimeError(f"❌ Database connection failed: {e}")
