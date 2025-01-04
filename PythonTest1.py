# 1) Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
input_string = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
binary_numbers = input_string.split(',')
divisible_by_5 = []
for binary in binary_numbers:
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        divisible_by_5.append(binary)
print(','.join(divisible_by_5))

# 2)Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
a = input("Enter a single digit value of a: ")
a1 = int(a)
a2 = int(a * 2)
print(a2)
a3 = int(a * 3)
print(a3)
a4 = int(a * 4)
print(a4)
result = a1 + a2 + a3 + a4
print("The result of a + aa + aaa + aaaa is:", result)

# 3)Write a program that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal
net_amount = 0
print("Enter transactions in the format 'D 100' for deposit and 'W 200' for withdrawal.")
print("Type 'done' when you are finished.")
while True:
    transaction = input("Enter transaction: ")
    if transaction.lower() == "done":
        break
    parts = transaction.split()
    action = parts[0]
    amount = int(parts[1])
    if action == "D":
        net_amount += amount
    elif action == "W":
        net_amount -= amount
print(f"The net amount in the bank account is: {net_amount}")

# 4) Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
n = int(input("Enter a positive integer n (n > 0): "))
sum_series = 0.0
for i in range(1, n + 1):
    sum_series += i / (i + 1)
print(f"The sum of the series for n = {n} is: {sum_series}")

# 5) Write a Python program to generate all permutations of a list in Python.
# Sample List = [1,2,3]

#6) Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_data = sorted(data, key=lambda x: float(x[1]), reverse=True)
print("Sorted Output:")
print(sorted_data)

# 7) Write a Python program to sort a list alphabetically in a dictionary.
# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# Sample Output: {'n1': [1, 2, 3], 'n3': [2, 3, 4], 'n2': [1, 2, 5]}
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key in num:
    num[key].sort()
print(num)

# 8) Define a class named American which has a static method called printNationality.
class American:
    @staticmethod
    def printNationality():
        print("I am American")
American.printNationality()

# 9) Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
def generate_and_print_squares():
    squares_list = [i ** 2 for i in range(1, 21)]
    print("First 5 elements of the squares list:")
    print(squares_list[:5])
generate_and_print_squares()
