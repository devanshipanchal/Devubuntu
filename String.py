# Python program to remove extra spaces from a given string(remove beginning and end spaces but keep one space in between words).
str = "  This is string  "
print(str.strip())

# Write a Python program to find the second most repeated word in a given string.
# To be done after dictionary
str1 = "this is a test string this is a test test string this test is"
words = str1.split()
count = []
max_repeated = []
for word in words:
    count.append(word)
    if word == word:
        max_repeated.append(word)
        print(len(max(max_repeated)))

# Write a Python program to find the smallest and largest word in a given string.
str2 = "this is a test string this is a test test string this test is"
words = str2.split()

smallest_words = words[0]
largest_words = words[0]

for word in words:
    if len(word) < len(smallest_words):
        smallest_words = word
    if len(largest_words) < len(word):
        largest_words = word
print("Smallest word in string is:", smallest_words)
print("Largest word in string is:", largest_words)

# Write a Python program to wrap a given string into a paragraph of given width.
str3 = "This is a sample string that we want to wrap into a paragraph of given width."
width = int(input("Enter the width of the paragraph:"))
wrapped_text = []
current_lines = ""
words = str3.split()
for word in words:
    if len(current_lines) + len(word) + 1 <= width:
        current_lines += "" + word
    else:
        wrapped_text.append(current_lines)
        current_lines = word
for line in wrapped_text:
    print(line)

# Write a Python program to swap cases of a given string.
str4 = "THIS SHOULD ALL BE LOWERCASE."
print(str4.swapcase())
print(str3.swapcase())

# Write a Python program to remove unwanted characters from a given string.
str5 = "  This , is : string  "
words = str5.split()
characters = [',', ':', '@', '.', '/']
emp =[]
cleaned_str = []
print(words)
for word in words:
    if word in characters:
        emp.append(word)
    else:
        cleaned_str.append(word)
print(cleaned_str)

# Write a Python program to remove the characters which have odd index values of a given string.
str6 = "Python is fun"
print(str6)
new_str = ""
for i in range(len(str6)):
    if i % 2 == 0:
        new_str += str6[i]
print(new_str)

# Python program to receive a string from the user and ask the user to add after which characters he wants to add a new line character.
str7 = input("Enter a string:")
new_line = []
while True:
    word = input("Enter words to have new line from :")
    if word == "":
        break
    new_line.append(word)
words = str7.split()
result_str = ""
for word in words:
    result_str += word + ""
    if word in new_line:
        result_str = result_str.strip() + '\n'
print(result_str)

# Python program to receive a string input from user and if there are any special character such as \n or \t then program should print the entered
# string with new line and with a tabular space
# # Receive input from user
# str8 = "Hello World /n This is a test string"
# # Initialize an empty string to hold the formatted output
# formatted_output = ""
# # Iterate through each character in the user input
# for char in str8:
#     print(char)
#     Check for newline character
#     if char == '/n':
#         formatted_output += "\\n\n"
#     print("Formatted Output:", formatted_output)
#     Check for tab character
#     elif char == '\t':
#         formatted_output += '\t'
#     else:
#         formatted_output += char