import psycopg2
import time
import random

# Database connection parameters
DB_CONFIG = {
    "host": "localhost",
    "database": "retail_db",
    "user": "cdc_user",
    "password": "password"
}

# Product list for random selection
PRODUCTS = [
    (101, "Laptop"), (102, "Smartphone"), (103, "Tablet"),
    (104, "Headphones"), (105, "Monitor"), (106, "Keyboard"),
    (107, "Mouse"), (108, "Smartwatch"), (109, "Speaker"),
    (110, "External HDD")
]

def insert_random_inventory():
    """Inserts random inventory data every 5 seconds."""
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        while True:
            product = random.choice(PRODUCTS)  # Select a random product
            product_id = product[0]
            quantity = random.randint(1, 50)  # Random stock quantity
            
            cursor.execute(
                "INSERT INTO inventory (product_id, quantity) VALUES (%s, %s);",
                (product_id, quantity)
            )
            connection.commit()

            print(f"Inserted: Product ID {product_id} - Quantity {quantity}")

            time.sleep(5)  # Wait for 5 seconds before the next insert

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_random_inventory()