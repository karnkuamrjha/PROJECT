"""
Customer Spending Analysis ⭐

An online company has customer names and their purchase amounts.

Task:

Calculate total spending for each customer.
Use filter() to find customers spending more than ₹50,000.
Use lambda with filter().

"""

from typeguard import value


customers = [
    {"name": "Rahul", "purchases": [15000, 20000, 18000]},
    {"name": "Priya", "purchases": [25000, 30000, 15000]},
    {"name": "Amit", "purchases": [10000, 12000, 8000]},
    {"name": "Neha", "purchases": [30000, 25000, 20000]},
    {"name": "Arjun", "purchases": [12000, 18000, 10000]}
]
print("========================================")
print("       CUSTOMER SPENDING ANALYSIS")
print("========================================")



def calculate_total_spending(*args):
    return sum(args)

total_spending=0

for customer in customers:
    total_spending = calculate_total_spending(*customer["purchases"])

    print("\n")
    print(customer["name"])
    print("TOTAL SPENDING :₹",total_spending)


print('\n')
print("----------------------------------------")
print("Customers Spending More Than ₹50,000")
print("----------------------------------------")


def high(*x):
    return sum(x)

for customer in customers:
    total=high(*customer["purchases"])
    result=list(filter(lambda x:x>50000,[total]))
    if result:
        print(customer["name"],"→ ",result[0])
    
        