"""
10. Complete Sales Analytics Project ⭐⭐⭐

A company provides sales data containing:

Order ID
Product
Category
Price
Quantity
Discount
Region

Task:

Calculate revenue for every order.
Calculate discount amount.
Calculate final revenue.
Find total revenue.
Find the highest-value order.
Find orders above ₹50,000.
Find unique product categories.
Use functions for calculations.
Use map() to transform sales data.
Use filter() and lambda to find high-value orders.

"""

sales = [
    {
        "order_id": 101,
        "product": "Laptop",
        "category": "Electronics",
        "price": 50000,
        "quantity": 2,
        "discount": 10,
        "region": "North"
    },
    {
        "order_id": 102,
        "product": "Smartphone",
        "category": "Electronics",
        "price": 25000,
        "quantity": 3,
        "discount": 5,
        "region": "South"
    },
    {
        "order_id": 103,
        "product": "Headphones",
        "category": "Accessories",
        "price": 3000,
        "quantity": 10,
        "discount": 8,
        "region": "East"
    },
    {
        "order_id": 104,
        "product": "Monitor",
        "category": "Electronics",
        "price": 15000,
        "quantity": 4,
        "discount": 10,
        "region": "West"
    },
    {
        "order_id": 105,
        "product": "Tablet",
        "category": "Electronics",
        "price": 30000,
        "quantity": 2,
        "discount": 5,
        "region": "North"
    },
    {
        "order_id": 106,
        "product": "Keyboard",
        "category": "Accessories",
        "price": 2000,
        "quantity": 5,
        "discount": 5,
        "region": "South"
    }
]
def range(*args):
    return sum(args)
total_revenue=0
discount=0
final_revenue=0
tp=0
tf=0
td=0

for sale in sales:
    print("order",sale["order_id"]," → ",sale["product"])
    total_revenue=sale["price"]*sale["quantity"]
    print('Revenue:',total_revenue)
    discount=(total_revenue*sale["discount"])/100
    print("Discount:",discount)
    final_revenue=total_revenue-discount
    print("final revenue:",final_revenue)
    print("\n")
    tp=tp+total_revenue
    td=td+discount
    tf=tf+final_revenue
    
print("--------------------------------------------------")
print("total revenue:",tp)
print("total discount:",td)
print("total final revenue:",tf)
print('--------------------------------------------------')



#maximum 
print("\n")
heighest=max(sales,key=lambda order:order["price"]*order["quantity"]-(order["discount"]*order["price"]*order["quantity"])/100)
red=heighest["price"]*heighest["quantity"]-(heighest["discount"]*heighest["price"]*heighest["quantity"])/100
print(heighest["order_id"],"→",heighest['product'],"→",red)


#find order above 50,000
print("\n")
print("Orders Above ₹50,000:")
print("\n")
itself = list(filter(
    lambda x: x["price"] * x["quantity"]
    - (x["price"] * x["quantity"] * x["discount"]) / 100 > 50000,
    sales
))

for x in itself:
    print(
        x["order_id"],
        "→",
        x["price"] * x["quantity"]
        - (x["discount"] * x["price"] * x["quantity"]) / 100
    )

#unique
print("\n")
print("Unique Categories:")
z=set()

for sale in sales:
    z.add(sale["category"])
   
#print(z)       output:{'Electronics', 'Accessories'}
"""
step1:create empty sets.
step2:Go through each sale
step 3:Get the category
step4:Add it to the set

"""

for b in z:
    print(b)

print("==================================================")