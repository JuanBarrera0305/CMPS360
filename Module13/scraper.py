from bs4 import BeautifulSoup
import os

def extract_products_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    products = []
    product_elements = soup.find_all('div', class_='product')
    
    for prod in product_elements:
        product = {
            'title': prod.find('h2', class_='title').text.strip(),
            'author': prod.find('p', class_='author').text.strip(),
            'price': prod.find('p', class_='price').text.strip(),
            'model/isbn': prod.find('p', class_='isbn').text.strip(),
            'rating': prod.find('p', class_='rating').text.strip(),
            'publisher': prod.find('p', class_='publisher').text.strip(),
            'pages/keys': prod.find('p', class_='pages').text.strip(),
            'language': prod.find('p', class_='language').text.strip(),
            'stock': prod.find('p', class_='stock').text.strip(),
            'description': prod.find('p', class_='description').text.strip(),
            'image': prod.find('img', class_='product-image')['src']
        }
        products.append(product)
    
    return products

# Paths to your local files (adjust if needed)
gadgets_file = 'gadgets.html'
keyboards_file = 'keyboards.html'

# Extract data
gadgets_data = extract_products_from_html(gadgets_file)
keyboards_data = extract_products_from_html(keyboards_file)

# Print sample output
print("🧠 Gadgets Sample:")
for item in gadgets_data[:2]:
    print(item, "\n")

print("⌨️ Keyboards Sample:")
for item in keyboards_data[:2]:
    print(item, "\n")

import json

# Save gadgets data to JSON
with open('gadgets.json', 'w', encoding='utf-8') as f:
    json.dump(gadgets_data, f, indent=2)

# Save keyboards data to JSON
with open('keyboards.json', 'w', encoding='utf-8') as f:
    json.dump(keyboards_data, f, indent=2)

print("✅ JSON files created: gadgets.json and keyboards.json")