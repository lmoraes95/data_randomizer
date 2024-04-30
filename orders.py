import psycopg2
import random
from faker import Faker

fake = Faker()

db_config = {
    'host': '127.0.0.1',
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': 'postgres'
}

def get_customer_ids(cursor):
    cursor.execute("SELECT CustomerID FROM Customers")
    return [row[0] for row in cursor.fetchall()]

def insert_order(cursor, order):
    insert_query = """
    INSERT INTO Orders (CustomerID, OrderDate, ShippingType, Segment) VALUES (%s, %s, %s, %s)
    RETURNING OrderID;
    """
    cursor.execute(insert_query, order)
    return cursor.fetchone()[0]

def generate_order_record(customer_ids):
    segment = random.choice(['Consumer', 'Corporate', 'Home Office'])
    return (
        random.choice(customer_ids),
        fake.date_time_between(start_date="-4y", end_date="now"), 
        random.choice(['Standard Class', 'Second Class', 'First Class', 'Same Day']),
        segment
    )

def main():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        customer_ids = get_customer_ids(cursor)
        if not customer_ids:
            raise Exception("No customer IDs found. Make sure the Customers table is populated.")

        for _ in range(539):
            order = generate_order_record(customer_ids)
            insert_order(cursor, order)

        conn.commit()
        print("Orders inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
