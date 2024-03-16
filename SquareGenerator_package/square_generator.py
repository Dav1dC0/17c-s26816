class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x ** 2 for x in range(start, end + 1)]


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            return []
        return [x ** 3 for x in range(start, end + 1)]

    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("Start of the range must be less than the end.")
        return super().generate_squares(start, end)

cubic_gen = CubicGenerator()

try:
    valid_squares = cubic_gen.generate_squares(1, 5)
    print("Valid squares:", valid_squares)

    invalid_squares = cubic_gen.generate_squares(5, 1)
    print("Invalid squares attempt:", invalid_squares)
except ValueError as e:
    print("Error:", e)