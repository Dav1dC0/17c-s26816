# File: main.py
from square_generator import SquareGenerator
import math

square_gen = SquareGenerator()

example_squares = square_gen.generate_squares(10, 1)
print("Attempt with end < start:", example_squares)

valid_example_squares = square_gen.generate_squares(1, 10)
print("Valid range example:", valid_example_squares)

square_roots = [math.sqrt(number) for number in valid_example_squares]
print("Square roots of valid range:", square_roots)