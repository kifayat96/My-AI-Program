# Code 3: Dictionary Example
student = {
    "name": "Ali",
    "age": 22,
    "semester": 5,
    "skills": ["Python", "AI"]
}

print(f"Student Name: {student['name']}")
print(f"Current Skills: {student['skills']}")

# Task: Aap code mein 'semester' ko change karein aur ek nayi skill add karein
student['semester'] = 6
student['skills'].append("GitHub")

print(f"Updated Student Profile: {student}")