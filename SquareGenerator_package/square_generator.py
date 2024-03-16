class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x**2 for x in range(start, end + 1)]

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            return []
        return [x**3 for x in range(start, end + 1)]

# Example usage of the CubicGenerator subclass
cubic_gen = CubicGenerator()

# Generate cubes from 1 to 5
cubes_list = cubic_gen.generate_cubes(1, 5)
print(cubes_list)