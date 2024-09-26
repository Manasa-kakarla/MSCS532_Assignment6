class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def __repr__(self):
        return str(self.data)

# Example usage
arr = Array()
arr.insert(1)
arr.insert(2)
arr.insert(3)
print(arr)  # Output: [1, 2, 3]
arr.delete(1)
print(arr.access(1))  # Output: 3
print(arr)  # Output: [1, 3]
