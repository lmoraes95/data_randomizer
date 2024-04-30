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

def get_category_mapping(cursor):
    cursor.execute("SELECT CategoryID, CategoryName FROM ProductCategories")
    return {row[1]: row[0] for row in cursor.fetchall()}

def insert_product(cursor, product):
    insert_query = """
    INSERT INTO Products (Name, CategoryID, Price, Cost) VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, product)

def main():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        category_mapping = get_category_mapping(cursor)
        if not category_mapping:
            raise Exception("No categories found. Make sure to run the ProductCategories script first.")

        products = [
            ("Office Chair", "Furniture", 150.00, 75.00),
            ("Office Table", "Furniture", 250.00, 125.00),
            ("Office Desk", "Furniture", 200.00, 100.00),
            ("Sofa", "Furniture", 500.00, 250.00),
            ("Bookshelf", "Furniture", 150.00, 75.00),
            ("Stationery Set", "Office Supplies", 20.00, 10.00),
            ("Paper", "Office Supplies", 5.00, 2.50),
            ("Desk Organizer", "Office Supplies", 25.00, 12.50),
            ("Markers", "Office Supplies", 10.00, 5.00),
            ("Ink", "Office Supplies", 30.00, 15.00),
            ("Laptop", "Technology", 1000.00, 500.00),
            ("Phone", "Technology", 700.00, 350.00),
            ("Headphones", "Technology", 150.00, 75.00),
            ("Tablet", "Technology", 400.00, 200.00),
            ("Projector", "Technology", 300.00, 150.00)
        ]

        for product in products:
            name, category_name, price, cost = product
            category_id = category_mapping.get(category_name)
            if category_id:
                insert_product(cursor, (name, category_id, price, cost))

        conn.commit()
        print("Products inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
