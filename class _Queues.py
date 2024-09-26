class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.data[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        return str(self.data)

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue)  # Output: [1, 2]
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
