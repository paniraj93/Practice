class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def values_to_tree(lst):
    if len(lst) == 0:
        return None
    mid = len(lst) // 2
    root = Node(lst[mid])
    root.left = values_to_tree(lst[:mid])
    root.right = values_to_tree(lst[mid+1:])
    return root

def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    lst = list(map(int, input("values saperated by space: ").split()))
    root = values_to_tree(lst)
    preorder_traversal(root)  # Output should be: 4 2 1 3 6 5 7
