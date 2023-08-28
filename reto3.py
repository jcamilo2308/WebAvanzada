"""Dado dos diccionarios 1 de productos y el 2 de categoría, conocer un 3 que permita tener el nombre del producto y el nombre de su categoría ejemplo."""
# Dictionary for categories
categories = {
    101: {
        "id": 101,
        "name": "Utiles escolares"
    },
    102: {
        "id": 102,
        "name": "Aseo"
    }
}

# Dictionary of products
products = {
    1: {
        "id": 1,
        "name": "Libreta",
        "price": 12.500,
        "id_cat": 101
    },
    2: {
        "id": 2,
        "name": "Jabón",
        "price": 10.500,
        "id_cat": 102
    }
}

# Create a dictionary to store matching products and categories
matching_products = {}

# Iterate through the products and match them with categories
for product_id, product_info in products.items():
    product_category_id = product_info["id_cat"]
    
    if product_category_id in categories:
        category_name = categories[product_category_id]["name"]
        product_name = product_info["name"]
        
        matching_products[product_id] = {
            "product": product_name,
            "category": category_name
        }

# Print the matching products and categories
print("Matching Products and Categories:")
for product_id, details in matching_products.items():
    print(f"Product ID: {product_id}, Product: {details['product']}, Category: {details['category']}")
