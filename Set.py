# Find the Differences Between Two Lists Using Sets
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
diff1 = set1 - set2
diff2 = set2 - set1
print("Difference of list1 and list2:", diff1)
print("Difference of list2 and list1:", diff2)

# Check if a Given String Is heterogram or Not
input_string = "The quick brown fox jumps"

normalized_string = ''.join(char.lower() for char in input_string if char.isalpha())

seen_characters = set()

heterogram = True
for char in normalized_string:
    if char in seen_characters:
        is_heterogram = False
        break
    seen_characters.add(char)

if heterogram:
    print(f'The string "{input_string}" is a heterogram.')
else:
    print(f'The string "{input_string}" is not a heterogram.')

# Find Maximum and Minimum Values of a Set
numbers = {4, 8, 1, 16, 3, 9, 2}
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value in set = ", max_value)
print("Minimum value in set = ", min_value)

# Determine if Two Sets Are Disjoint or Not Without In-built Methods
set3 = {1, 2, 3, 4}
set4 = {5, 6, 7, 8}

are_disjoint = True
for element in set3:
    if element in set4:
        are_disjoint = False
        break

if are_disjoint:
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")

# Remove the Given Items of a Set at Once
set5 = {1, 2, 3, 4, 5, 6}
remove_items = {3, 5}
for items in remove_items:
    if items in set5:
        set5.remove(items)
print("Updated set: ", set5)

# Count Number of Vowels in a Given String Using Sets
str = "Hello, World!"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
count = 0
for char in str:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string are: {count}")

# Convert a Set to String
string_set = {"apple", "banana", "cherry"}
result_string = ', '.join(string_set)
print(f"The set as a string: {result_string}")

# Find Common Elements of Three Given Lists Using Sets
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
set6 = set(list1)
set7 = set(list2)
set8 = set(list3)
common_elements = (set6 & set7 & set8)
common_elements_list = list(common_elements)
print(f"Common elements in all three lists: {common_elements_list}")

# Square the Elements of Set Using for Loop
set9 = {1, 2, 3, 4, 5}
squared_set = set()
for element in set9:
    squared_set.add(element ** 2)
print(f"The set with squared elements: {squared_set}")

# Check if a Set Is Superset Itself or Another Given Set
set10 = {1, 2, 3, 4, 5}
set11 = {2, 3, 4}
is_superset_of_itself = True
is_superset_of_set11 = True
for element in set11:
    if element not in set10:
        is_superset_of_set11 = False
        break
print(f"set10 is a superset of itself: {is_superset_of_itself}")
print(f"set10 is a superset of set11: {is_superset_of_set11}")

# Perform Intersection of Two Lists Using Set Methods
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
set1 = set(list1)
set2 = set(list2)
intersection = set1.intersection(set2)
intersection_list = list(intersection)
print(f"The intersection of the lists is: {intersection_list}")

# Check if a Given Value Is Present in the Set or Not
my_set = {1, 2, 3, 4, 5}
value = int(input("Enter a value to check in set: "))
if value in my_set:
    print(f"The value {value} is present in the set.")
else:
    print(f"The value {value} is not present in the set.")
