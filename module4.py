n = int(input("Enter N: "))

print(f"Please enter {n} numbers, one by one:")
numbers = []
for i in range(n):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

x = int(input("Enter X: "))

print(numbers.index(x) + 1 if x in numbers else -1)
