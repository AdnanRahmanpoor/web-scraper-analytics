import psycopg2
from psycopg2.extras import DictCursor
from config.settings import DATABASE

class DatabaseConnection:
    # Initialize database connection with the connection parameters
    def __init__(self):
        self.conn_params = {
            'dbname': DATABASE['NAME'],
            'user': DATABASE['USER'],
            'password': DATABASE['PASSWORD'],
            'host': DATABASE['HOST'],
            'port': DATABASE['PORT']
        }

    # Connect to the database
    def __enter__(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self.conn.cursor(cursor_factory=DictCursor)

    # Disconnect from the database
    def __exit__(self, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

# Initialize database tables
def init_db():
    with DatabaseConnection() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                price DECIMAL(10,2),
                description TEXT,
                category VARCHAR(100),
                url VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

# Insert product into the database
def insert_product(product_data):
    with DatabaseConnection() as cursor:
        cursor.execute("""
            INSERT INTO products (title, price, description, category, url)
            VALUES (%(title)s, %(price)s, %(description)s, %(category)s, %(url)s)
            RETURNING id
        """, product_data)
        return cursor.fetchone()[0]