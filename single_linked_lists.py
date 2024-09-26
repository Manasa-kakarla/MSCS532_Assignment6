class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        raise ValueError("Value not found in the list")

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def __repr__(self):
        return " -> ".join(map(str, self.traverse()))

# Example usage
linked_list = SinglyLinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
print(linked_list)  # Output: 3 -> 2 -> 1
linked_list.delete(2)
print(linked_list)  # Output: 3 -> 1
