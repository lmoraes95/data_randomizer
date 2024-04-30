import psycopg2
from faker import Faker
import random
import requests
import re

fake = Faker()

db_config = {
    'host': '127.0.0.1',
    'dbname': 'ecommerce',
    'user': 'postgres',
    'password': 'postgres'
}

def get_real_address():
    city = fake.city()
    response = requests.get(
        'https://nominatim.openstreetmap.org/search',
        params={'city': city, 'country': 'USA', 'format': 'json', 'limit': 1},
        headers={'User-Agent': 'YourAppName'}
    )
    if response.status_code == 200:
        data = response.json()
        if data:
            result = data[0]
            street_address = result.get('display_name')
            postal_code = result.get('address', {}).get('postcode')
            return {
                'street_address': street_address, 
                'city': result.get('address', {}).get('city', city),
                'state': result.get('address', {}).get('state'),
                'country': 'United States',
                'latitude': result.get('lat'),
                'longitude': result.get('lon'),
                'postal_code': postal_code 
            }
    return None


def insert_customer(cursor, customer):
    insert_query = """
    INSERT INTO Customers (
        FirstName, LastName, Email, Phone, StreetAddress, City, State, Country,
        Latitude, Longitude, PostalCode, DateOfBirth, RegistrationDate, IsActive
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, customer)

def generate_customer_record():
    address_info = get_real_address()
    if address_info:
        return (
            fake.first_name(),
            fake.last_name(),
            fake.email(),
            fake.phone_number()[:20],
            address_info['street_address'],
            address_info['city'],
            address_info['state'],
            address_info['country'],
            address_info['latitude'],
            address_info['longitude'],
            address_info['postal_code'], 
            fake.date_of_birth(minimum_age=18, maximum_age=90),
            fake.date_time_this_decade(),
            fake.boolean()
        )
    else:
        return None

def main():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        num_records = 5000

        for _ in range(num_records):
            customer = generate_customer_record()
            if customer:
                insert_customer(cursor, customer)

        conn.commit()

        print(f"{num_records} customer records inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
