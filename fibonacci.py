#fibonacci#
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(6))

# SUM OF DIGIT # 1
y=int(input("enter the number"))
def sum_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digit(n // 10)
print("sum of digit is",sum_digit(y))
    
    
# def sum_digit(n):
#     digits = [int(digit) for digit in str(n)]  # Create a list of digits
#     return sum(digits)

# print(sum_digit(1234))  # Output: 10def sum_digit(n):


