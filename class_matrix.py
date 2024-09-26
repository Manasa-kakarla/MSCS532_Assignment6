class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            self.data[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def get_value(self, row, col):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            return self.data[row][col]
        else:
            raise IndexError("Index out of bounds")

    def __repr__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

# Example usage
mat = Matrix(2, 3)
mat.set_value(0, 0, 1)
mat.set_value(1, 2, 5)
print(mat)  # Output: 1 0 0 \n 0 0 5
