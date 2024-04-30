import psycopg2

db_config = {
    'host': '127.0.0.1',
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': 'postgres'
}

def insert_product_category(cursor, category_name):
    insert_query = """
    INSERT INTO ProductCategories (CategoryName) VALUES (%s);
    """
    cursor.execute(insert_query, (category_name,))

def main():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        categories = ['Furniture', 'Office Supplies', 'Technology']
        for category in categories:
            insert_product_category(cursor, category)

        conn.commit()
        print("Product categories inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
