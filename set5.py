# Code 5: Raw Data Cleaning
# Ye raw data hai jisme numbers repeat ho rahe hain
raw_data = [10, 20, 10, 30, 40, 20, 50, 50]

print(f"Raw Data: {raw_data}")

# Step 1: Set banao (Duplicates khatam)
clean_set = set(raw_data)

# Step 2: Wapis List bana lo
clean_data = list(clean_set)

print(f"Clean Data: {clean_data}")

# Task: raw_data mein kuch aur duplicate numbers daal kar check karein.