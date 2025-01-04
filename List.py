# multiple ways of determining variable data type like integer, string or list.
test = [1, "hello", 2.13, "bye"]
print("type of list is:", type(test[1]))

print("type of numm is:", type(test[2]))

# sum all the items in a list(without inbuilt functions).
num1 = [1, 2, 2, 2.14]
sum = 0
for i in num1:
    sum += i
    print(sum)

# square all the items in a list.
for i in num1:
    power = i ** 2
    print(power)

# multiply all the items in a list(without inbuilt functions).
multi = 1
for i in num1:
    multi *= i
    print(multi)

# print the second maximum number from a list of numbers(without inbuilt functions).
list1 = [10, 50, 60, 20, 40]
list1.sort()
print("Second largest element in list is: ", list1[-2])

# Write a python program to add integer values into a list.
#     Add value at the beginning of the list if the value is odd.
#     Add value at the end of the list if the value is even.
num = int(input("Entre a number:"))
list2 = [2, 3, 4]
if num % 2 == 0:
    list2.append(num)
    print("List is:", list2)
else:
    list2.insert(0, num)
    print("List is:", list2)

# find and count how many times value is repeated in the list(without inbuilt functions).
lst = [1, 2, 3, 4, 5, 4, 3, 5, 3, 1, 3, 5, 7, 6, 3, 2, 1, 5, 7, 6, 6]
num2 = int(input("Enter a value to count:"))
count = 0
for i in lst:
    if i == num2:
        count += 1
print("Count of given element is: ", count)

# Write a python program to filter out the list of numbers that are odd and even
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_lst = []
even_lst = []
for i in lst1:
    if i % 2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(odd_lst)
print(even_lst)

# Write a python program to determine if the switch is on or off,
#   - use the given truth table for checking values and showing results.
main_input = [0, 1, 0, 0, 1, 1, 1, 1]
input1 = [0, 1, 1, 1, 0, 0, 1, 1]
input2 = [0, 1, 0, 1, 0, 1, 0, 1]
result = [1, 0, 0, 0, 0, 1, 1, 1]
switch = []
for i in range(len(main_input)):
    if main_input[i] == input1[i] and main_input[i] == input2[i]:
        switch.append(result[i])
for i in switch:
    if switch[i] == 0:
        print("Switch is off")
    elif switch[i] == 1:
        print("Switch is on")
    else:
        print("No data available")

# find three numbers from an array such that the sum of three numbers equal to zero.
nums = [-1, 0, 1, 2, -1, -4]
triplets = []
for num in range(len(nums)):
    if num >= 0:
        triplets.append(num)
        print(triplets)
    else:
        print("Triplets not possible")

# find the single element in a list where every element appears three times except for one
in3 = [5, 3, 4, 3, 5, 5, 3]
emp_lst = []
counts = []
for num in in3:
    if num in emp_lst:
        indice = emp_lst.index(num)
        counts[indice] += 1
        print(in3)
    else:
        emp_lst.append(num)
        counts.append(1)
repeated = counts.index(max(counts))
repeated_ele = emp_lst[repeated]
print("Most repeated number", repeated_ele)

# Write a Python program to push all zeros to the end of a list.
list3 = [0, 2, 3, 4, 6, 7, 10]
for i in list3:
    if i == 0:
        list3.pop(i)
        # print("popped element", list3)
        list3.append(i)
        print("List with zeroes at last", list3)
        break

# Write a Python program to find majority element in a list.
inp = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
unique_elements = []
counts = []
for num in inp:
    if num in unique_elements:
        a = unique_elements.index(num)
        counts[a] += 1
    else:
        unique_elements.append(num)
        counts.append(1)
repeated_element_index = counts.index(max(counts))
repeated_element = unique_elements[repeated_element_index]
print("Majority element:", repeated_element)

#  Write a Python program to find the length of the last word.
str = ["Python", "Exercises"]
print("len of last word", len("Exercises"))

# Finding the Middle Element in a List
numList = [1, 2, 3, 4, 5]
middle_index = len(numList)//2
middle_element = numList[middle_index]
print("Middle Element is: ", middle_element)

# Write a Python program to print all prime numbers in an interval.
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))
primeList = []
for num in range(start, end+1):
    if num > 1:
        prime_no = True
        for i in range(2, int((num ** 0.5) + 1)):
            if num % i == 0:
                print("Not a prime number.")
            else:
                primeList.append(num)
                break
print(f"Prime numbers between {start} and {end} are {primeList}")

# Python program which counts the vowels from the list, and find the maximum and minimum count of the vowel of them.
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
