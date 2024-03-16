from cubic_generator import CubicGenerator

cubic_gen = CubicGenerator()

try:
    valid_squares = cubic_gen.generate_squares(1, 5)
    print("Valid squares:", valid_squares)

    invalid_squares = cubic_gen.generate_squares(5, 1)
    print("Invalid squares:", invalid_squares)
except ValueError as e:
    print("Error:", e)