#1. Write a Python function that takes string from the user and return the longest word and the length of the longest one.
str2 = input("Enter a string: ")
words = str2.split()
largest_words = words[0]
for word in words:
    if len(largest_words) < len(word):
        largest_words = word
print("Largest word in string is:", largest_words, f"\nLength of largest word is:" ,len(largest_words))

# 2. Write a Python program that takes input from the user and compute the sum of digits of a given string.
input_string = input("Enter a string containing digits: ")
sum_of_digits = 0
for char in input_string:
    if char.isdigit():
        sum_of_digits += int(char)
print(f"The sum of digits in '{input_string}' is: {sum_of_digits}")

# 3. Write a Python program to find the majority element in a list (without use of inbuilt function).
# Input : [1, 2, 3, 4, 5, 5, 5, 6, 5, 5, 6, 4,2,]
test_lst = [1, 2, 3, 4, 5, 5, 5, 6, 5, 5, 6, 4, 2]
unique_elements = []
counts = []
for num in test_lst:
    if num in unique_elements:
        a = unique_elements.index(num)
        counts[a] += 1
    else:
        unique_elements.append(num)
        counts.append(1)
repeated_element_index = counts.index(max(counts))
repeated_element = unique_elements[repeated_element_index]
print("Majority element:", repeated_element)

# 4. Write a Python program to remove an empty tuple(s) from a list of tuples.
# [1, 2, 3, ’aa’, ‘bb’, (), (10, 11), ‘123’, (‘ ‘), ‘a’, [1, ’b’, (1,2)]]

# 5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the
# form (x, x*x).Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = int(input("Enter a number (n > 0): "))
result_dict = {}
for x in range(1, n + 1):
    result_dict[x] = x * x
print("Generated Dictionary:", result_dict)

# 6. Write a Python function to reverse a string if its length is a multiple of 4
def reverse_if_multiple_of_four(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s
test_string = input("Enter a string:")
print(reverse_if_multiple_of_four(test_string))

# 7. Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = [item for item in list1 if item not in list2]
print("Difference between list1 and list2:", difference)

# 8. Write a python program which counts the vowels from the list, and find the maximum and minimum
# count of the vowel of them.
# List = [‘a’, ‘b’, ‘c’, ‘a’, ‘a’, ‘e’, ‘z’, ‘u’, ‘u’ ‘x’, ‘g’, ‘j, ‘A’, ‘b’, ‘O’, 0, ‘U’, ‘U’, ‘u’, ‘d’, ‘m’, ’i’, ‘i’, ‘i’, ‘o’, ’u’, ’o’ ,’u’]
letters = ['a', 'b', 'c', 'a', 'a', 'e', 'z', 'u', 'u', 'x', 'g', 'j', 'A', 'b', 'o', 0, 'U', 'U', 'u', 'd', 'm', 'i', 'i', 'i', 'o', 'u', 'o', 'u']
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_count = []
for letter in letters:
    if letter in vowels:
        vowel_count.append(letter)
print("Number of vowels in list: ", vowel_count)
print("Count of total no. of vowels", len(vowel_count))
print("maximum repeated vowel", max(vowel_count))
print("minimum repeated vowel", min(vowel_count))

# 9.write a python program which validates user registration form with validations.
# Fields : name, mobile, email(only accept alphanumeric, (. dot), and @ and .com should be predefined
# end of the email), pin(not more than 6 digit)

# 10. Write a python program which switch dictionary key to value and value to key:
# Ex : {‘a’: 1, ‘b’: 10}
# Result : {1 : ‘a’, 10: ‘b’}
original_dict = {'a': 1, 'b': 10}
switched_dict = {value: key for key, value in original_dict.items()}
print("Original dictionary:", original_dict)
print("Switched dictionary:", switched_dict)

# 11. Write a python program which generates the given below pattern.
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
