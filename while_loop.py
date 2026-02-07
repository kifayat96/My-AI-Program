# Code 3: Battery Charger
battery = 90

print("Charging started...")

# Jab tak battery 100 se kam hai, loop chalta rahega
while battery < 100:
    battery += 2  # Har baar 2% charge badhao
    print(f"Battery is at: {battery}%")

print("Fully Charged!")

# Task: battery = 90 ko change karke 50 karein.