import requests
from bs4 import BeautifulSoup
import json

# Files to scrape
urls = ['books.html']  # Only scrape books.html
data = []

for file in urls:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        # Debug: Print the soup to inspect the HTML
        print(soup.prettify())  # This will show the structured HTML
        
        products = soup.find_all('div', class_='product')
        
        # Check if we are finding products
        if not products:
            print(f"No products found in {file}")
        
        for p in products:
            data.append({
                "title": p.find(class_="title").text if p.find(class_="title") else None,
                "author": p.find(class_="author").text if p.find(class_="author") else None,
                "price": p.find(class_="price").text if p.find(class_="price") else None,
                "isbn": p.find(class_="isbn").text if p.find(class_="isbn") else None,
                "rating": p.find(class_="rating").text if p.find(class_="rating") else None,
                "publisher": p.find(class_="publisher").text if p.find(class_="publisher") else None,
                "pages": p.find(class_="pages").text if p.find(class_="pages") else None,
                "language": p.find(class_="language").text if p.find(class_="language") else None,
                "stock": p.find(class_="stock").text if p.find(class_="stock") else None,
                "description": p.find(class_="description").text if p.find(class_="description") else None,
            })

# Save to JSON
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("✅ Scraping complete. Data saved to products.json.")
