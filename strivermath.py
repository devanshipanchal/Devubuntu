#COUNT THE DIGITS#
# n=int(input("enter the digit: "))
# def count_digits(n):
#     num_str=str(n)

#     y=len(num_str)
#     return y
# print(count_digits(n))
# print()

# num=int(input("enter the digits : "))
# def count_digits(num):
#     # Step 1: Handle negative numbers
#     num = abs(num)
    
#     # Step 2: Initialize a counter
#     count = 0
    
#     # Step 3: Count the digits
#     if num == 0:
#         return 1  # Special case for zero
#     while num > 0:
#         num //= 10  # Integer division by 10
#         count += 1  # Increment the counter
    
#     return count
# print(count_digits(num))

def count_digit(n):
    count=0
    lasdigi=[]
    while n>0:
        lasdigi=n%10
        count=count+1
        n=n/10
    print(lasdigi)
print(count_digit)


