"""
5. Product Price Transformation

An e-commerce company wants to increase all product prices by 10%.

Task:

Store product prices in a list.
Use map() and lambda to calculate the new prices.
Display the old and new prices.

"""

prices = [1000, 2500, 5000, 7500, 10000]

increase_percentage = 10


print("========================================")
print("  PRODUCT PRICE TRANSFORMATION")
print("========================================")


# calculate new price using map() and lambda

new_price=list(map(lambda x: x + (x * increase_percentage / 100), prices))

for old,new in zip(prices,new_price):
    print(f"old price:{old}  → new prices:{new}")


print("\n")
print("========================================")
print("price increased :10%")
print("========================================")