
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x**2 for x in range(start, end + 1)]