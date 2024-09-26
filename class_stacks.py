class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        return str(self.data)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack)  # Output: [1, 2]
print(stack.pop())  # Output: 2
print(stack.peek())  # Output: 1
