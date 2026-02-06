# Code 4: Looping through Dict
prices = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 3000
}

print("Product List:")
# .items() humein Key aur Value dono deta hai
for item, price in prices.items():
    print(f"{item} ki qeemat hai: {price} PKR")

# Task: Is loop mein Tax add karke print karein (price + 500).