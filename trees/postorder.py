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

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')  # Print node value here for postorder

if __name__ == "__main__":
    lst = list(map(int, input("values separated by space: ").split()))
    root = values_to_tree(lst)
    postorder_traversal(root)
    print()  # Add a newline for better output formatting
