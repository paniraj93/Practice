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

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

if __name__ == "__main__":
    lst = list(map(int, input("values saperated by space: ").split()))
    root = values_to_tree(lst)
    inorder_traversal(root)  # Output should be the sorted list: 1 2 3 4 5 6 7
    