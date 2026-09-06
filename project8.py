from itertools import product


products = {
    "product1": {
        "name": "Laptop",
        "category": "Electronics",
        "price": 50000,
        "stock": 15
    },
    "product2": {
        "name": "Mouse",
        "category": "Accessories",
        "price": 800,
        "stock": 7
    },
    "product3": {
        "name": "Keyboard",
        "category": "Accessories",
        "price": 2000,
        "stock": 5
    },
    "product4": {
        "name": "Monitor",
        "category": "Electronics",
        "price": 15000,
        "stock": 12
    },
    "product5": {
        "name": "Printer",
        "category": "Electronics",
        "price": 12000,
        "stock": 8
    }
}

print("========================================")
print("          INVENTORY ANALYSIS")
print("========================================")

#find unique categories of products
categories = [product["category"] for product in products.values()]
unique_categories = set(categories)
print("unique category:")

for cat in unique_categories:
    print(cat)

print("\n")

for product in products.values():
    if product["stock"] < 10:
        print(f"{product["name"]} → stock:{product["stock"]}")


count=0

for product in products.values():
    if product["stock"]<10:
        count = count+1

print("\n")
print("========================================")        
print("Total Low Stock Products:",count)
print("========================================")