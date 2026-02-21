student_marks = {
    "Akshit": 85,
    "Rahul": 78,
    "Priya": 92,
    "Anjali": 88,
    "Rohan": 74,
    "Sneha": 90,
    "Karan": 81,
    "Meera": 95
}


name = input("Enter the student's name: ").strip().title()


if name in student_marks :
    print(f"{name}'s marks:{student_marks[name]}")
else:
    print(f"{name} is not found in record")
    
