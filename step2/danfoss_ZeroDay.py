import os  # For accessing environment variables
import sys  # For system-specific parameters and functions
import psycopg2 as dbapi2  # PostgreSQL database interaction

# SQL statements to initialize the database tables
INIT_STATEMENTS = [
    """
    create table if not exists users(
        id serial primary key,
        username varchar not null unique,
        password varchar not null
    )
    """,
    """
    create table if not exists video(
        id serial primary key,
        name varchar not null,
        url varchar not null,
        likes integer default 0 not null,
        dislikes integer default 0 not null
    )
    """,
    """
    ALTER TABLE users ADD COLUMN IF NOT EXISTS is_admin BOOLEAN DEFAULT FALSE
    """,
    """
    create table if not exists requirements(
        id serial primary key,
        name varchar not null
    )
    """
]

# Initialize the database with the given URL
def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()

# Function to get all requirements
def get_all_requirements():
    """Retrieve all requirements from the requirements table."""
    query = "SELECT id, name FROM requirements"
    with dbapi2.connect(os.getenv("DATABASE_URL")) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        requirements = cursor.fetchall()
    return requirements

# Main execution to run the initialization
if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python danfoss_ZeroDay.py")
        sys.exit(1)
    initialize(url)