#half pyramid
n = int(input("Enter number rows: "))
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()

#Reverse half pyramid
m = int(input("Enter number rows: "))
for i in range(m):
    for j in range(m-i):
        print("* ", end="")
    print()

#String Half pyramid
string = input("Enter a string:")
string_len = len(string)
for i in range(string_len, 0, -1):
    for j in range(i):
        print(string[j], end=" ")
    print()

# Full pyramid
n = int(input("Enter number of rows: "))  # User inputs the number of rows
for i in range(n):                          # Loop through each row
    # Print spaces
    for j in range(n - i - 1):            # Print leading spaces
        print(" ", end=" ")
    # Print stars
    for j in range(2 * i + 1):             # Print stars for the current row
        print("*", end=" ")
    print()                                  # Move to the next line after each row
