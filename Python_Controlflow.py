# Python code demonstrating control flow

# 1. if-elif-else
number = int(input("Enter a number: "))

if number > 0:
    print("It's a positive number.")
elif number < 0:
    print("It's a negative number.")
else:
    print("It's zero.")

# 2. for loop with continue
print("\nEven numbers from 1 to 10 (using for loop):")
for i in range(1, 11):
    if i % 2 != 0:
        continue  # Skip odd numbers
    print(i, end=' ')
print()

# 3. while loop with break
print("\nCounting up to 5 (using while loop):")
count = 1
while True:
    print(count)
    if count == 5:
        break  # Exit loop when count reaches 5
    count += 1
