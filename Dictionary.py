# Write a python program to switch places of key value in a dictionary.
original_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print("Original dictionary:", original_dict)
swapped_dict = {}
# Iterate over the original dictionary items
for key, value in original_dict.items():
    # Swap the key and value and add to the new dictionary
    swapped_dict[value] = key
print("Swapped dictionary:", swapped_dict)

# Write a python program to update a value in a dictionary with a specified key
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)
dict1['c'] = 4
print(dict1)

# Write a python program to update a value in a dictionary with a specified value.

dict2 = {'a': 1, 'b': 2, 'c': 3}
# Print the original dictionary
print("Original dictionary:", dict2)

# Specify the key and the new value
update_key = 'b'
new_value = 20

if update_key in dict2:
    dict2[update_key] = new_value
    print(f"Updated the value of '{update_key}' to {new_value}.")
else:
    print(f"Key '{update_key}' not found in the dictionary.")

print("Updated dictionary:", dict2)

# Write a python program to generate a dictionary from two lists
# Lst1 = [‘Bhaskar’, ’Vishal’, ‘Dhara’]
# Lst2 = [[‘apple’,’orange’], [‘banana’,’weat floor’], [‘butter milk’,’apple juice’]]
# Receive this two lists from user
# And create one dictionary like below.
# {Bhaskar’: [‘apple’,’orange’], ‘Vishal’: [‘banana’,’weat floor’], ‘Dhara’: [‘butter milk’,’apple juice’]}

# Receive input from user for the first list
lst1 = input("Enter the first list of names separated by commas: ").split(',')

# Receive input from user for the second list of lists
lst2 = []
print("Enter the second list of lists (comma-separated values within semicolons):")
for i in range(len(lst1)):
    sublist = input(f"Enter the list for {lst1[i].strip()}: ").split(',')
    lst2.append([item.strip() for item in sublist])

# Create the dictionary by zipping the two lists together
result_dict = dict(zip(lst1, lst2))

# Print the resulting dictionary
print("Generated dictionary:")
print(result_dict)

# Write a python program to manage employee detail in dictionary.
# Example: {‘name’: ‘Bhaskar’, ‘mobile’: 9876543210, ‘city’: ‘Gandhinagar’, ‘email’: ‘bhaskar@mail.local’}

employee_details = {}

name = input("Enter employee's name: ")
mobile = input("Enter employee's mobile number: ")
city = input("Enter employee's city: ")
email = input("Enter employee's email: ")

employee_details['name'] = name
employee_details['mobile'] = mobile
employee_details['city'] = city
employee_details['email'] = email

print("Employee Details: \n", employee_details)

# Write a python program to manage product’s pricelist.
# Keep asking for key until the user enters nothing.
# Enter product(key) and its price(value)
# Entering key that is already added it should update the value with available key value pair.
# Print the dictionary in tabular format

pricelist = {}
while True:
    product = input("Enter product name (or press Enter to finish): ").strip()
    if product == "":
        break
    price = float(input(f"Enter price for {product}: ").strip())
    pricelist[product] = price
print("\nProduct Pricelist:")
print(f"{'Product':} {'Price':}")
for product, price in pricelist.items():
    print(f"{product:} {price:}")

# Write a python program to merge two dictionaries.
# Receive key and value input from user do that for 2 dictionaries.
dict1 = {}
dict2 = {}
while True:
    key = input("Enter key (or press Enter to finish): ").strip()
    if key == "":
        break
    value = input(f"Enter value for {key}: ").strip()
    dict1[key] = value
# dict2[key] = value
print("Dictionary-1: \n", dict1)
while True:
    key = input("Enter key (or press Enter to finish): ").strip()
    if key == "":
        break
    value = input(f"Enter value for {key}: ").strip()
    dict2[key] = value
print("Dictionary-2: \n", dict2)
dict1.update(dict2)
print("Merged dictionary: \n", dict1)