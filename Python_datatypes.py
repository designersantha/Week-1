# Python code using user input with various data types

# Integer input
age = int(input("Enter your age (integer): "))
print("Integer:", age, "| Type:", type(age))

# Float input
height = float(input("Enter your height (float): "))
print("Float:", height, "| Type:", type(height))

# String input
name = input("Enter your name (string): ")
print("String:", name, "| Type:", type(name))

# Boolean input
is_student_input = input("Are you a student? (yes/no): ").strip().lower()
is_student = is_student_input == "yes"
print("Boolean:", is_student, "| Type:", type(is_student))

# List input
fruits_input = input("Enter some fruits separated by commas: ")
fruits = fruits_input.split(",")
fruits = [fruit.strip() for fruit in fruits]  # remove whitespace
print("List:", fruits, "| Type:", type(fruits))

# Tuple input
coords_input = input("Enter two coordinates separated by a comma (e.g., 10.5, 20.3): ")
x, y = map(float, coords_input.split(","))
coordinates = (x, y)
print("Tuple:", coordinates, "| Type:", type(coordinates))

# Set input
numbers_input = input("Enter some numbers separated by spaces (duplicates will be removed): ")
numbers = set(map(int, numbers_input.split()))
print("Set:", numbers, "| Type:", type(numbers))

# Dictionary input
name_key = input("Enter a key for name: ")
name_value = input("Enter a value for name: ")
age_key = input("Enter a key for age: ")
age_value = int(input("Enter a value for age: "))
person = {name_key: name_value, age_key: age_value}
print("Dictionary:", person, "| Type:", type(person))

# NoneType
nothing = None
print("NoneType:", nothing, "| Type:", type(nothing))
