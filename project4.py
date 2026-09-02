"""
3. Student Performance Analysis

Store marks for 5 subjects for multiple students.

Task:

Calculate total and average marks.
Assign grades using conditional statements.
Use a loop to process every student.
Use a function to calculate the average.
"""

students = [
    {
        "name": "Rahul",
        "math": 85,
        "science": 90,
        "english": 78,
        "computer": 95,
        "social_science": 88
    },

    {
        "name": "Priya",
        "math": 92,
        "science": 88,
        "english": 95,
        "computer": 90,
        "social_science": 91
    },

    {
        "name": "Amit",
        "math": 65,
        "science": 72,
        "english": 68,
        "computer": 75,
        "social_science": 70
    },

    {
        "name": "Neha",
        "math": 55,
        "science": 62,
        "english": 58,
        "computer": 65,
        "social_science": 60
    }
]

print("========================================")
print("       STUDENT PERFORMANCE ANALYSIS")
print("========================================")





total_marks=0
average_marks=0
grade=0

for student in students:
    for key,value in student.items():
        total_marks=student['math']+student["science"]+student["english"]+student["computer"]+student["social_science"]
        average_marks=total_marks/5
        if average_marks>=90:
            grade="A+"
        elif average_marks>=80:
            grade="A"
        elif average_marks>=70:
            grade="B"
        elif average_marks>=60:
            grade="C"
        else:
         grade="D"


    print("\nNAME:",student["name"])
    print("\nMATH:",student["math"])
    print("SCIENCE:",student["science"])
    print("ENGLISH:",student["english"])
    print("COMPUTER:",student["computer"])
    print("SOCIAL SCIENCE:",student["social_science"])
    print("\nTOTAL MARKS:",total_marks)
    print("AVERAGE MARKS:",average_marks)
    print("GRADE:",grade)
    print("\n----------------------------------------")
