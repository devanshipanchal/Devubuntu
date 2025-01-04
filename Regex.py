import re

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
pattern = r'[A-Z][a-z]*'
text = "Here are some TestSequences to Match: Apple, Banana, Cat, and dog."
sequences = re.findall(pattern, text)
print("Sequences found:", sequences)

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
string = "a...b "   # a123b ab.
pattern = r'^a.*b$'
matches = re.findall(pattern, string)
print("Matches found:", matches)

# Write a Python program that matches a word at the end of string, with optional punctuation.
str = "word, another-word,"
pattern = r'\b\w+\b[.,:!?]?'
match = re.search(pattern, str)
print("Matches found: ", match.group())

# Write a Python program that matches a word at the beginning of a string.
str = "word another-word,"
pattern = r'^\b\w+\b'
match = re.search(pattern, str)
print("Matches found: ", match.group())

# Write a Python program that matches a word containing 'z', not at the start or end of the word.
str = "amazing pizza"
pattern = r'\b\w+[^z\s]z[^z\s]\w*\b'
match = re.findall(pattern, str)
print("Matches found: ", match)

# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
str = "1 23 456"
pattern = r'\b\d{1,3}\b'
match = re.findall(pattern, str)
print("Matches found: ", match)

# Write a Python program to remove leading zeros from an IP address
ip = '192.168.001.001'
pattern = r'\b0+(\d)'
replace = re.sub(pattern, r'\1', ip)
print("New ip: ", replace)

# Write a Python program to replace whitespaces with an underscore and vice versa.
string1 = 'abc 12\ de 23 \n f45 6'
string2 = 'abc_12\_de_23_\n_f45_6'
pattern1 = '\s+'
replace = '_'
replace_ = ' '
new_string = re.sub(pattern1, replace, string1)
replace_underscore = re.sub(r'_', replace_, string2)
print(new_string)
print(replace_underscore)

# Write a Python program to search some literals strings in a string.
str2 = "Here are some fruits: apple, banana, cherry, and date."
pattern = ["apple", "banana", "cherry", "date"]
for items in pattern:
    print(f"Pattern: {items}")
    if re.search(items, str2):
        print("It is a match.")
    else:
        print("Not a match.")

# Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = 'fox'
print(f"Word searched: {searched_words}")
match = re.search(searched_words, sample_text)
if match:
    print("It is a match.", match.span())
else:
    print("Not a match.")

# Write a Python program to find all three, four, five characters long words in a string.
str3 = "Here are some words of various lengths: cat, dog, bird, snake, elephant, lion, tiger, ant."
pattern = r'\b\w{3,5}\b'
match = re.findall(pattern, str3)
print("Matches found: ", match)

# Write a python program to convert snake case string to camel case string and vice versa.
snake_case_string = "this_is_a_snake_case_string"
camel_case_string = "thisIsACamelCaseString"
#snake case to camel case
parts = snake_case_string.split('_')
titled = parts[0]+''.join(word.title() for word in parts[:])
print(titled)
#camel case to snake case
snake_case = re.sub(r'(?<!^)([A-Z])', r'_\1',camel_case_string).lower()
print(snake_case)

# Write a Python program to extract values between quotation marks of a string
text = 'He said, "Hello, how are you?" and then she replied, "I am fine, thank you!".'
pattern = r'"(.*?)"'
matches = re.findall(pattern, text)
print("Values between quotation marks:", matches)

# Write a Python program to insert spaces between words starting with capital letters
text = "ThisIsASampleStringWithCapitalLetters"
pattern = r'(?<!^)([A-Z])'
result = re.sub(pattern, r' \1', text)
print("String with spaces between words:", result)
