# Code 4: Default Values
def describe_pet(pet_name, animal_type="cat"):
    print(f"I have a {animal_type}.")
    print(f"Its name is {pet_name}.")

# Case 1: Sirf naam diya (Type khud 'cat' manega)
describe_pet("Mano")

# Case 2: Dono cheezein di
describe_pet("Sheru", "dog")

# Task: Ek naya janwar (bird) aur uska naam dekar call karein.