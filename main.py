import os
import psycopg2
import psycopg2.extras
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()


def get_db():
    """Create and return a new PostgreSQL connection and cursor."""
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
    DB_PORT = result.port if result.port else 5432

    if not all([DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT]):
        raise ValueError("❌ One or more database credentials are missing!")

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            sslmode="require"
        )
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return connection, cursor
    except Exception as e:
        raise RuntimeError(f"❌ Database connection failed: {e}")
