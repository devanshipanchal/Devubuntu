# Add, mul, sub, div using function
def Add(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum of numbers: ", result)
Add(1, 2, 3, 4, 5)

def Sub(num1, num2):
    subtraction = num1 - num2
    print("Subtraction of two numbers: ", subtraction)
Sub(83,75)

def Multi(num1, num2):
    multiplication = num1 * num2
    print("Multiplication of two numbers: ", multiplication)
Multi(15,12)

def Div(num1, num2):
    division = num1 // num2
    print("Division of two numbers: ", division)
Div(50,25)

# find the avg num of marks
def Avg_marks(*marks):
    addition = 0
    for mark in marks:
        addition = addition + mark
        average = addition // len(marks)
        print("Average of marks: ", average)
Avg_marks(85, 92, 75, 64, 86, 95)

# function to compute grade
grades = []
def Grades(*marks):
    for mark in marks:
        if mark <= 50:
            grades.append("Fail")
        elif mark >= 60:
            grades.append("D")
        elif mark >= 70:
            grades.append("C")
        elif mark >= 80:
            grades.append("B")
        elif mark >= 90:
            grades.append("A")
Grades(41, 52, 63, 76, 82, 95, 50)
print(grades)

# Write a Python program to check if a string is a palindrome using function
def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s == s[::-1]
test_string = "A man, a plan, a canal, Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')

# Write a Python program to print all prime numbers in an interval using function
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def print_primes_in_interval(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
print(f"Prime numbers between {start} and {end} are: ")
print_primes_in_interval(start, end)

# Write a Python function that takes string from the user and return the longest word and the length of the longest one.
def find_longest_word(s):
    words = s.split()
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word, max_length
input_string = input("Enter a string: ")
longest_word, length_of_longest_word = find_longest_word(input_string)
print(f"The longest word is: '{longest_word}' with length: {length_of_longest_word}")

# Write a Python function to reverse a string if its length is a multiple of 4
string = input("Enter a string: ")
def reverse_string(s):
    length_of_string = len(s)
    if length_of_string // 4:
        print("The reversed String is: ", s[::-1])
    else:
        print("Length of string is not a multiple of 4")
reversed_string = reverse_string(string)
