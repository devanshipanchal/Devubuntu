# Python program to check if a string is a palindrome.
while True:
    input_string = input("Enter a string to check if it is a palindrome (or press Enter to exit): ")
    if input_string == "":
        break
    cleaned_string = input_string.replace(" ", "")
    # Reverse the string
    reversed_string = cleaned_string[::-1]
    if cleaned_string == reversed_string:
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")
