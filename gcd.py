
# def gec():
#     m = int(input("Enter the first number: "))
#     n = int(input("Enter the second number: "))
#     cf = []
#     for i in range(1, min(m, n) + 1):
#         if m % i == 0 and n % i == 0:
#             cf.append(i)
#             print(cf)
#     return cf[-1]

# print("The GCD is:", gec())

# def gec():
#     m = int(input("Enter the first number: "))
#     n = int(input("Enter the second number: "))
    
#     for i in range(1, min(m, n) + 1):
#         if m % i == 0 and n % i == 0:
#          y=i
#     return y
# print("The GCD is:", gec())

def factors(n):
   f1=[]
   for i in range(1,n+1):
       if n%i==0:
           f1.append(i)
   return f1

def prime(n):
    return(factors(n)==[1,n])



number = 7
print(f"The factors of {number} are: {factors(number)}")
print(f"Is {number} a prime number? {'Yes' if prime(number) else 'No'}")

def factors(n):
    f1 = []
    for i in range(1, n + 1):
        if n % i == 0:
            f1.append(i)
    return f1  # Fixed indentation

def prime(n):
    return factors(n) == [1, n]

number = 7
print(f"The factors of {number} are: {factors(number)}")
print(f"Is {number} a prime number? {'Yes' if prime(number) else 'No'}")



