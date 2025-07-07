# Python program demonstrating error handling

def divide_numbers():
    try:
        # Get input from the user
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        # Try dividing
        result = num1 / num2

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")
    
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")

    else:
        # Runs only if no exception occurred
        print(f"✅ The result is: {result}")

    finally:
        # Runs no matter what
        print("👉 Division operation attempted.\n")

# Call the function
divide_numbers()
