import psycopg2
import random

db_config = {
    'host': '127.0.0.1',
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': 'postgres'
}

def get_order_and_product_ids(cursor):
    cursor.execute("SELECT OrderID FROM Orders")
    order_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT ProductID FROM Products")
    product_ids = [row[0] for row in cursor.fetchall()]

    return order_ids, product_ids

def insert_order_detail(cursor, order_detail):
    insert_query = """
    INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s);
    """
    cursor.execute(insert_query, order_detail)

def generate_order_detail_record(order_ids, product_ids):
    order_id = random.choice(order_ids)
    product_id = random.choice(product_ids)
    quantity = random.randint(1, 10)

    return (order_id, product_id, quantity)

def main():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        order_ids, product_ids = get_order_and_product_ids(cursor)
        if not order_ids or not product_ids:
            raise Exception("No orders or products found. Make sure the Orders and Products tables are populated.")

        for _ in range(539):
            order_detail = generate_order_detail_record(order_ids, product_ids)
            insert_order_detail(cursor, order_detail)

        conn.commit()
        print("Order details inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
