class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        return self.numbers.index(x) + 1 if x in self.numbers else -1


n = int(input("Enter N: "))

print(f"Please enter {n} numbers, one by one:")
number_list = NumberList()
for i in range(n):
    number_list.insert(int(input(f"Enter number {i + 1}: ")))

x = int(input("Enter X: "))

print(number_list.search(x))
