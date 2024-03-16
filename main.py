import math

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x**2 for x in range(start, end + 1)]

square_gen = SquareGenerator()

example_squares = square_gen.generate_squares(10, 1)
print("Attempt with end < start:", example_squares)

valid_example_squares = square_gen.generate_squares(1, 10)
print("Valid range example:", valid_example_squares)

square_roots = [math.sqrt(number) for number in valid_example_squares]
print("Square roots of valid range:", square_roots)