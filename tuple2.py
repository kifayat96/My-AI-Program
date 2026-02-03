# Code 2: Set Example
# Student ID ki list jisme kuch duplicates hain
student_ids = [101, 102, 103, 101, 104, 102]

print(f"List with duplicates: {student_ids}")

# List ko Set mein convert karein
unique_ids = set(student_ids)

print(f"Set (Duplicates removed): {unique_ids}")

# Task: Isme naya ID add karke dekhein
unique_ids.add(105)
print(f"After adding 105: {unique_ids}")