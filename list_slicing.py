# a list number form 0 to 9
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", my_list)
# Slicing the list to get elements from index 2 to 5
sliced_list = my_list[2:6]
print("Sliced list (index 2 to 5):", sliced_list)
# Slicing the list to get every second element
every_second_element = my_list[::2]
print("Every second element:", every_second_element)
# Slicing the list to get elements in reverse order
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)
# Slicing the list to get elements from index 5 to the end
from_index_5 = my_list[5:]
print("Elements from index 5 to end:", from_index_5)
# Slicing the list to get elements from the start to index 4
to_index_4 = my_list[:5]
print("Elements from start to index 4:", to_index_4)
# Slicing the list to get elements from index 3 to 7 with a step of 2
step_slice = my_list[3:8:2]
print("Elements from index 3 to 7 with step 2:", step_slice)
# Slicing the list to get the last three elements
last_three_elements = my_list[-3:]
print("Last three elements:", last_three_elements)
# Slicing the list to get elements from index -7 to -3
mid_negative_slice = my_list[-7:-3]
print("Elements from index -7 to -3:", mid_negative_slice)
# Slicing the list to get every third element
every_third_element = my_list[::3]
print("Every third element:", every_third_element)
# Slicing the list to get elements from index 1 to 8 with a step of 3
custom_step_slice = my_list[1:9:3]
print("Elements from index 1 to 8 with step 3:", custom_step_slice)

# Slicing the list to get elements from index 4 to 2 (should return an empty list)
empty_slice = my_list[4:2]
print("Elements from index 4 to 2 (empty slice):", empty_slice)
# Slicing the list to get elements from index 8 to 3 in reverse order
reverse_custom_slice = my_list[8:2:-1]
print("Elements from index 8 to 3 in reverse order:", reverse_custom_slice)

# Slicing the list to get elements from index 0 to 9 with a step of 4
custom_step_large = my_list[0:10:4]
print("Elements from index 0 to 9 with step 4:", custom_step_large)
