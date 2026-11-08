import numpy as np


class KNNRegressor:
    def __init__(self, n, k):
        self.k = k
        self.points = np.empty((n, 2), dtype=float)  # column 0: x, column 1: y
        self.count = 0

    def insert(self, x, y):
        self.points[self.count] = [x, y]
        self.count += 1

    def predict(self, x):
        if self.k > self.count:
            raise ValueError(f"k ({self.k}) must be less than or equal to N ({self.count}).")
        distances = np.abs(self.points[:, 0] - x)
        nearest = np.argsort(distances, kind="stable")[: self.k]
        return np.mean(self.points[nearest, 1])


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive integer.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a real number.")


n = read_positive_int("Enter N: ")
k = read_positive_int("Enter k: ")

print(f"Please enter {n} points (x, y), one by one:")
model = KNNRegressor(n, k)
for i in range(n):
    x = read_float(f"Point {i + 1} - enter x: ")
    y = read_float(f"Point {i + 1} - enter y: ")
    model.insert(x, y)

x = read_float("Enter X: ")

try:
    print(f"Y = {model.predict(x)}")
except ValueError as e:
    print(f"Error: {e}")
