class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]

square_gen = SquareGenerator()
example_squares = square_gen.generate_squares(1, 10)
print(example_squares)