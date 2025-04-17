import json
import psycopg2

# Load JSON data
with open('keyboards.json', 'r', encoding='utf-8') as f:
    keyboards = json.load(f)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname='scraperdbmod13',
    user='postgres',
    # password='your_password',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

# Insert each keyboard into the table
for k in keyboards:
    cur.execute("""
        INSERT INTO keyboards (
            title, author, price, model_isbn, rating,
            publisher, pages_keys, language, stock, description, image
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        k['title'],
        k['author'],
        k['price'],
        k['model/isbn'],
        float(k['rating']),
        k['publisher'],
        k['pages/keys'],
        k['language'],
        k['stock'],
        k['description'],
        k['image']
    ))

# Commit and close
conn.commit()
cur.close()
conn.close()

print("✅ Keyboard data imported successfully into PostgreSQL.")
