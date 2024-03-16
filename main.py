import math

class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]

square_gen = SquareGenerator()

squares_list = square_gen.generate_squares(1, 10)

square_roots = [math.sqrt(number) for number in squares_list]

print("Squares list:", squares_list)

print("Square roots list:", square_roots)