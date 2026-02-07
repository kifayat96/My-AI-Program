# Code 4: Skip and Stop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        print("Skipping 5 (Continue)")
        continue  # 5 ko print nahi karega, wapis upar jayega
    
    if num == 8:
        print("Stopping at 8 (Break)")
        break  # Loop yahi khatam ho jayega
    
    print(f"Processing number: {num}")

# Task: Break condition ko change karke num == 9 karein.