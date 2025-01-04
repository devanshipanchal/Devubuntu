#FOR LOOP
#For loop for printing list items
languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for i in languages:
    print(i)

#Print the string
a = "Language"
for i in a:
    print(i)

#print numbers from 0-20
for i in range(21):
    print(i)

#setting a range
for i in range(15, 21):
    print(i)

#printing all items in the list and executing else part
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
else:
    print("no elements")

#WHILE LOOP

#print even numbers from user input
num = int(input("Enter a number: "))
while num >= 0:
    if ( num % 2 == 0 ):
        print("\n", num, end='')
    num = num - 1

# Calculate the sum of numbers until user enters 0
number = int(input('Enter a number: '))
total = 0
# iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))
print('The sum is', total)

#Infinite loop
age = 32
# the test condition is always True
while age > 18:
    print('You can vote')
