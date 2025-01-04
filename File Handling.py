# 1. Copy a Binary File to new file
source_file_path = '/home/prasuk/Downloads/Binaryfile.bin'
destination_file_path = '/home/prasuk/Downloads/Binaryfile2.bin'
with open(source_file_path, 'rb') as source_file, open(destination_file_path, 'wb') as destination_file:
    file_contents = source_file.read()
    destination_file.write(file_contents)
print("File copied successfully.")


# 2.Remove Blank Lines from a File
source_file_path = '/home/prasuk/Downloads/Textfile1.txt'
destination_file_path = '/home/prasuk/Downloads/Textfile2.txt'
with open(source_file_path, 'r') as source_file, open(destination_file_path, 'w') as destination_file:
    for line in source_file:
        if line.strip():
            destination_file.write(line)
print("Blank lines removed successfully.")


# 3. Reverse Lines in a File
source_file_path = '/home/prasuk/Downloads/Textfile1.txt'
destination_file_path = '/home/prasuk/Downloads/Textfile2.txt'
with open(source_file_path, 'r') as source_file:
    lines = source_file.readlines()
reversed_lines = lines[::-1]
with open(destination_file_path, 'w') as destination_file:
    for line in reversed_lines:
        destination_file.write(line)
print("Lines reversed successfully.")


# 4. Count Words in a File
source_file_path = '/home/prasuk/Downloads/Textfile1.txt'
word_count = 0
with open(source_file_path, 'r') as source_file:
    for line in source_file:
        words = line.split()
        word_count += len(words)
print(f"Total number of words: {word_count}")


# 5. Find and Replace in a File
file_path = '/home/prasuk/Downloads/Textfile1.txt'
text_to_find = 'Lorem'
text_to_replace = 'Unwanted'
with open(file_path, 'r') as file:
    file_contents = file.read()
new_contents = file_contents.replace(text_to_find, text_to_replace)
with open(file_path, 'w') as file:
    file.write(new_contents)
print("Text replaced successfully.")


# 6. Merge Two Files
source_file_path1 = '/home/prasuk/Downloads/Textfile1.txt'
source_file_path2 = '/home/prasuk/Downloads/Textfile3.txt'
destination_file_path = '/home/prasuk/Downloads/Textfile2.txt'
with open(destination_file_path, 'w') as destination_file:
    with open(source_file_path1, 'r') as source_file1:
        for line in source_file1:
            destination_file.write(line)
    with open(source_file_path2, 'r') as source_file2:
        for line in source_file2:
            destination_file.write(line)
print("Files merged successfully.")


# 7. Count Character Frequency in a File
source_file_path = '/home/prasuk/Downloads/Textfile1.txt'
char_frequency = {}
with open(source_file_path, 'r') as file:
    for line in file:
        for char in line:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
for char, count in char_frequency.items():
    print(f"Character '{char}' occurs {count} times")

