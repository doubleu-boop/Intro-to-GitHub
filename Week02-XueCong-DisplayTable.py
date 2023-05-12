#XueCong
#s10257059

import math

numbers = [1, 2, 3, 4, 5]
squares = []
square_roots = []

for i in numbers:
    squares.append(i**2)
    square_roots.append(math.sqrt(i))



words = ["One", "Two", "Three", "Four", "Five"]

print("{:>6}  {:^5}  {:^11}  {:>7}".format("Number", "Square", "Square root", "English"))

for (number, square, square_root, word) in zip(numbers, squares, square_roots, words):
    print("{:>6}  {:^6}  {:^11.2f}  {:>7}".format(number, square, square_root, word))
