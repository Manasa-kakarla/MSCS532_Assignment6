class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Add a child node to the current node."""
        self.children.append(child_node)

    def __repr__(self):
        return f"Node({self.value})"

class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, parent_value, child_value):
        """Add a child node under a specified parent node."""
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            new_node = Node(child_value)
            parent_node.add_child(new_node)
        else:
            raise ValueError(f"Parent node with value {parent_value} not found.")

    def find_node(self, current_node, target_value):
        """Recursively find a node with the specified value."""
        if current_node.value == target_value:
            return current_node
        for child in current_node.children:
            result = self.find_node(child, target_value)
            if result:
                return result
        return None

    def traverse(self, node=None):
        """Traverse the tree and return a list of node values."""
        if node is None:
            node = self.root
        
        values = [node.value]
        for child in node.children:
            values.extend(self.traverse(child))
        return values

    def __repr__(self):
        return " -> ".join(map(str, self.traverse()))

# Example usage
if __name__ == "__main__":
    tree = Tree("Root")
    tree.add_node("Root", "Child 1")
    tree.add_node("Root", "Child 2")
    tree.add_node("Child 1", "Child 1.1")
    tree.add_node("Child 1", "Child 1.2")
    tree.add_node("Child 2", "Child 2.1")

    print(tree)  # Output: Root -> Child 1 -> Child 1.1 -> Child 1.2 -> Child 2 -> Child 2.1
