from module5_mod import NumberList

n = int(input("Enter N: "))

print(f"Please enter {n} numbers, one by one:")
number_list = NumberList()
for i in range(n):
    number_list.insert(int(input(f"Enter number {i + 1}: ")))

x = int(input("Enter X: "))

print(number_list.search(x))
