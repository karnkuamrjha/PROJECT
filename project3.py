"""
3. Employee Salary Analysis

A company has employee name, department, salary, experience, and performance score.

"""

employees = [
    {
        "name": "Rahul",
        "department": "Data Analytics",
        "salary": 60000,
        "experience": 3,
        "performance_score": 92
    },

    {
        "name": "Priya",
        "department": "Finance",
        "salary": 55000,
        "experience": 4,
        "performance_score": 78
    },

    {
        "name": "Amit",
        "department": "Marketing",
        "salary": 45000,
        "experience": 2,
        "performance_score": 65
    },

    {
        "name": "Neha",
        "department": "HR",
        "salary": 50000,
        "experience": 5,
        "performance_score": 88
    }
]

print("========================================")
print("       EMPLOYEE SALARY ANALYSIS")
print("========================================")




bonus=0
c=0
total_salary=0
annual_salary=0

for employee in employees:
    for key,value in employee.items():
        annual_salary=employee["salary"]*12
        if employee["performance_score"]>90:
            bonus=(employee["salary"]*12*15)/100
            c="excellent performance"
        elif employee["performance_score"]>=75:
            bonus=(employee["salary"]*12*10)/100
            c="good performance"
        elif employee["performance_score"]>=60:
            bonus=(employee["salary"]*12*5)/100
            c="average performance"
        else:
            bonus=employee["salary"]*12
            c="poor performance"

        total_salary=annual_salary+bonus
         


    print('\nname:',employee['name'])
    print("department:",employee["department"])
    print("experience:",employee["experience"])
    print("monthly salary:",employee["salary"])
    print("annual salary:",annual_salary)
    print("performance score:",employee["performance_score"])
    print("\nbonus:",bonus)
    print("performance categroy:",c)
    print("total annual salary:",total_salary)
    print("\n----------------------------------------")

print("\n========================================")