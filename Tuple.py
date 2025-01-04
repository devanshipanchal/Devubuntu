# Create a tuple with the following elements: 1, 2, 3, 4, 5. Then, print the first and last elements.
tup1 = (1, 2, 3, 4, 5)
print(type(tup1))
print("First element", tup1[0])
print("Last element", tup1[-1])

# Create a tuple with mixed data types (e.g., integer, string, and float). Access and print each element.
tup2 = (1, "hello", 1.2)
for i in tup2:
    print("\n", i)

# Given a nested tuple ((1, 2), (3, 4), (5, 6)), print the second element of the first nested tuple.
tup3 = ((1, 2), (3, 4), (5, 6))
print("Second element of first nested tuple is:", tup3[0][1])

# Unpack the tuple ('apple', 'banana', 'cherry') into three variables and print them.3
tup4 = ('apple', 'banana', 'cherry')
fruit1, fruit2, fruit3 = tup4
print(fruit1)
print(fruit2)
print(fruit3)

# Given a tuple my_tuple = (10, 20, 30, 40, 50), iterate through the tuple and print each element.
tup4 = (10, 20, 30, 40, 50)
for i in tup4:
    print(i)

# Create a tuple with duplicate elements and find and print the count of a specific element (1, 2, 3, 3, 3, 4, 5).
tup5 = (1, 2, 3, 3, 3, 4, 5)
print("max number in tuple:", max(tup5))
print("max number in tuple:", tup5.count(3))

# Given a tuple of numbers (10, 20, 30, 40, 50), calculate and print the sum of all the elements.
tup6 = (10, 20, 30, 40, 50)
count = sum(tup6)
print(count)
