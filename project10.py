"""
Create employee records containing:

Name
Department
Salary
Experience

Task:

Use a list of dictionaries.
Use a set to find unique departments.
Use filter() to find employees earning more than ₹60,000.
Use map() to calculate annual salaries.
Use lambda with map() and filter().
"""

employees = [
    {
        "name": "Rahul",
        "department": "Data Analytics",
        "salary": 60000,
        "experience": 3
    },
    {
        "name": "Priya",
        "department": "Finance",
        "salary": 75000,
        "experience": 5
    },
    {
        "name": "Amit",
        "department": "Marketing",
        "salary": 55000,
        "experience": 2
    },
    {
        "name": "Neha",
        "department": "HR",
        "salary": 65000,
        "experience": 4
    },
    {
        "name": "Arjun",
        "department": "Data Analytics",
        "salary": 85000,
        "experience": 6
    }
]
print("========================================")
print('       EMPLOYEE DEPARTMENT ANALYSIS')
print("========================================")
print("\n")





#find unique departments

departments = set()

for employee in employees:
    departments.add(employee["department"])


for depart in departments:
    print(depart)


# Employees Earning More Than ₹60,000:
print("\n")
new = list(filter(lambda employee: employee["salary"] > 60000, employees))
for employee in new:
    print(f'{employee["name"]}→ {employee["salary"]}')


#annual salaries
print("\n")
def old(x):
    return x * 12

itself = list(map(
    lambda employee: {
        "name": employee["name"],
        "annual_salary": old(employee["salary"])
    },
    employees
))

for employee in itself:
    print(f'{employee["name"]} → {employee["annual_salary"]}')

print("\n")
print("========================================")