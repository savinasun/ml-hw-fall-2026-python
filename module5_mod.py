class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        return self.numbers.index(x) + 1 if x in self.numbers else -1
