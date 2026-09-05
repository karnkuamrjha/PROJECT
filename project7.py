"""
Sales Data Filtering

A company has a list of sales amounts:

sales = [12000, 45000, 75000, 15000, 90000, 32000]

Task:

Use filter() and lambda to find sales above ₹40,000.
Calculate the total of those sales.
Use variables and operators for the calculations.
"""

print("========================================")
print("        SALES DATA FILTERING")
print("========================================")

print("\n")
sales = [12000, 45000, 75000, 15000, 90000, 32000]

def total_sales(*args):
    return sum(args) 

new_sales=list(filter(lambda x: x > 40000, sales))

total=total_sales(*new_sales)

for sale in new_sales:
    print(sale)

print("\n")
print("total sales above 40,000:",total)

print("\n")
print("========================================")