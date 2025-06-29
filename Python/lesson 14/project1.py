import os

# Define the base file path
base_file_path = "C:\\Users\\hp\\Desktop\\Codingal\\Python\\lesson 14\\"
sample_doc_path = os.path.join(base_file_path, "sample_doc.txt")
my_file_path = os.path.join(base_file_path, "My_File.txt") # Assuming .txt extension for My_File

my_introduction = "Hello, this is a brief introduction. I am learning file handling in Python."

# 1. Open the file using the with() function and write your brief introduction in the file.
try:
    with open(sample_doc_path, 'w') as file:
        file.write(my_introduction)
    print(f"1. Successfully wrote introduction to '{sample_doc_path}'.")
except Exception as e:
    print(f"Error in step 1: {e}")

print("\n" + "="*40 + "\n")

# 2. Split the contents of the file into words and print all the words.
try:
    with open(sample_doc_path, 'r') as file:
        content = file.read()
        words = content.split() # Splits by whitespace by default
        print(f"2. Words from '{sample_doc_path}':")
        for word in words:
            print(word)
except FileNotFoundError:
    print(f"Error in step 2: '{sample_doc_path}' not found.")
except Exception as e:
    print(f"Error in step 2: {e}")

print("\n" + "="*40 + "\n")

# 3. Check whether a file named My_File.exists or not.
print(f"3. Checking if '{my_file_path}' exists:")
if os.path.exists(my_file_path):
    print(f"   '{my_file_path}' exists.")
else:
    print(f"   '{my_file_path}' does NOT exist.")

print("\n" + "="*40 + "\n")

# 4. Create a file with the same name if it doesn't exist and write your brief introduction in the file.
print(f"4. Creating/writing to '{my_file_path}' if it doesn't exist:")
if not os.path.exists(my_file_path):
    try:
        with open(my_file_path, 'w') as file:
            file.write(my_introduction)
        print(f"   '{my_file_path}' did not exist, so it was created and introduction written.")
    except Exception as e:
        print(f"   Error creating/writing to '{my_file_path}': {e}")
else:
    print(f"   '{my_file_path}' already exists. Skipping creation and writing.")

print("\n" + "="*40 + "\n")

# 5. Delete the file named sample_doc.
#    Assuming "sample_doc" refers to "sample_doc.txt" as per your provided path.
print(f"5. Deleting '{sample_doc_path}':")
if os.path.exists(sample_doc_path):
    try:
        os.remove(sample_doc_path)
        print(f"   Successfully deleted '{sample_doc_path}'.")
    except Exception as e:
        print(f"   Error deleting '{sample_doc_path}': {e}")
else:
    print(f"   '{sample_doc_path}' does not exist, no need to delete.")

# 6. Close the file wherever required.
# As explained in the previous response, the 'with open(...) as file:' statement automatically
# handles closing the file, which is the recommended practice. So no explicit close() calls are needed.
print("\n" + "="*40 + "\n")
print("6. File closing is handled automatically by 'with open(...) as file:' statements.")