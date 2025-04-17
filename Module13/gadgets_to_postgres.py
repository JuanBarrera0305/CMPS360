import json
import psycopg2

# Load JSON data
with open('gadgets.json', 'r', encoding='utf-8') as f:
    gadgets = json.load(f)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname='scraperdbmod13',
    user='postgres',
    # password='your_password',  # Uncomment and set if needed
    host='localhost',
    port='5432'
)

cur = conn.cursor()

# Insert each gadget into the table
for g in gadgets:
    cur.execute("""
        INSERT INTO gadgets (
            title, author, price, model_isbn, rating,
            publisher, pages_keys, language, stock, description, image
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        g['title'],
        g['author'],
        g['price'],
        g['model/isbn'],
        float(g['rating']),
        g['publisher'],
        g['pages/keys'],
        g['language'],
        g['stock'],
        g['description'],
        g['image']
    ))

# Commit and close
conn.commit()
cur.close()
conn.close()

print("✅ Data imported successfully into PostgreSQL.")
