import psycopg2
import json

conn = psycopg2.connect(
    dbname="scraperdb",  
    user="postgres",  # Your username (default is 'postgres')
    #password="yourpassword",  
    host="localhost",  # If PostgreSQL is running locally
    port="5432"  
)


cur = conn.cursor()

with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

    for product in products:
        cur.execute("""
            INSERT INTO products (title, author, price, isbn, rating, publisher, pages, language, stock, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            product["title"],
            product["author"],
            product["price"],
            product["isbn"],
            product["rating"],
            product["publisher"],
            product["pages"],
            product["language"],
            product["stock"],
            product["description"]
        ))

conn.commit()

cur.close()
conn.close()

print("✅ Data successfully inserted into PostgreSQL.")
