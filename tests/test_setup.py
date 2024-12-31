import sys

sys.path.insert(0, "/home/adnanrp/Projects/web-scraper-analytics/")

from src.utils.database import DatabaseConnection, init_db

def test_setup():
    #Initialize database tables
    print('Initializing database...')
    init_db()

    # Test Connection
    print("Testing database connection...")

    try:
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT 1")
            print("✓ Database connection successful!")

            # Check if tables were created
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
            """)
            tables = cursor.fetchall()
            print("✓ Available tables:", [table[0] for table in tables])

    except Exception as e:
        print("✗ Database connection failed:", str(e))

if __name__ == "__main__":
    test_setup()