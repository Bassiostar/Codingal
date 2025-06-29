file_path = "C:\\Users\\hp\\Desktop\\Codingal\\Python\\lesson 14\\sample_file.txt"

# 1) Open the file and print the contents of the file
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("--- Contents of the file ---")
        print(content)
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n" + "="*40 + "\n") # Separator

# 2) Print the first 10 characters of the file
try:
    with open(file_path, 'r') as file:
        file.seek(0) # Ensure we are at the beginning of the file
        first_10_chars = file.read(10)
        print("--- First 10 characters of the file ---")
        print(first_10_chars)
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n" + "="*40 + "\n") # Separator

# 3) Print the first line of the file
try:
    with open(file_path, 'r') as file:
        first_line = file.readline()
        print("--- First line of the file ---")
        print(first_line.strip()) # .strip() removes leading/trailing whitespace including newline
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n" + "="*40 + "\n") # Separator

# 4) Prints the first four lines of the file
try:
    with open(file_path, 'r') as file:
        print("--- First four lines of the file ---")
        for i in range(4):
            line = file.readline()
            if not line:  # Break if there are fewer than 4 lines
                break
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n" + "="*40 + "\n") # Separator

# 5) Loop through the contents of the file and print all the lines one by one
try:
    with open(file_path, 'r') as file:
        print("--- All lines of the file (one by one) ---")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 6) Close the file wherever required
# The 'with open(...) as file:' statement automatically handles closing the file,
# even if errors occur. This is the recommended way to work with files in Python.