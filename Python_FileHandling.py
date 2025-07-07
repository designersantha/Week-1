# Step 1: Create a file
filename = "my_file.txt"
with open(filename, 'w') as file:
    file.write("File created successfully.\n")
print("✅ Step 1: File created.")

# Step 2: Ask the user to write something
user_append = input("\n✍️ Step 2: Enter text to append to the file: ")

# Step 3: Append what the user wrote
with open(filename, 'a') as file:
    file.write(user_append + "\n")
print("✅ Step 3: Text appended.")

# Step 4: Read the file
print("\n📄 Step 4: Reading file content:")
with open(filename, 'r') as file:
    content = file.read()
    print(content)

# Step 5: Ask the user to overwrite something
user_overwrite = input("\n✍️ Step 5: Enter text to overwrite the file: ")

# Step 6: Overwrite the file with the user's input
with open(filename, 'w') as file:
    file.write(user_overwrite + "\n")
print("✅ Step 6: File overwritten.")

# Step 7: Final Read
print("\n📄 Step 7: Final file content:")
with open(filename, 'r') as file:
    final_content = file.read()
    print(final_content)
