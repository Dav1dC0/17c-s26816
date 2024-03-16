from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            return []
        return [x**3 for x in range(start, end + 1)]

    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("Start of the range must be less than the end.")
        return [x**2 for x in range(start, end + 1)]