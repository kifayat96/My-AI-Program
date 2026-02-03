# Code 4: List of Dictionaries
class_data = [
    {"id": 1, "name": "Hamza", "marks": 85},
    {"id": 2, "name": "Bilal", "marks": 90},
    {"id": 3, "name": "Sarah", "marks": 88},
]

# Loop chalakar sabke naam print karna
print("Student Names:")
for student in class_data:
    print(student['name'])

# Task: Is list mein apna data add karein (Change this code)
my_data = {"id": 4, "name": "Mera Naam", "marks": 95}
class_data.append(my_data)

print(f"Total Students: {len(class_data)}")
print(class_data)