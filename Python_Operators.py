# Simple Python code using operators with user input

# Get input from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Arithmetic Operators
sum_result = a + b        # Addition
diff = a - b              # Subtraction
product = a * b           # Multiplication
quotient = a / b if b != 0 else "Undefined (division by zero)"
modulus = a % b if b != 0 else "Undefined (modulus by zero)"

# Comparison Operators
is_equal = a == b         # Equal to
is_greater = a > b        # Greater than

# Logical Operators
logical_and = (a > 0) and (b > 0)
logical_or = (a < 0) or (b > 0)

# Output the results
print("\nResults:")
print("Addition:", sum_result)
print("Subtraction:", diff)
print("Multiplication:", product)
print("Division:", quotient)
print("Modulus:", modulus)
print("Are a and b equal?", is_equal)
print("Is a greater than b?", is_greater)
print("Logical AND result (a > 0 and b > 0):", logical_and)
print("Logical OR result (a < 0 or b > 0):", logical_or)
