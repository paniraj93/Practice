class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1  # Initialize height for AVL properties

def update_height(node):
    if not node:
        return 0
    node.height = 1 + max(find_height(node.left), find_height(node.right))
    return node.height

def get_balance(node):
    if not node:
        return 0
    return find_height(node.left) - find_height(node.right)

def bst(val, root):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = bst(val, root.left)
    elif val > root.val:
        root.right = bst(val, root.right)
    else:
        return root

    update_height(root)

    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and val < root.left.val:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and val > root.right.val:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and val > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and val < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def find_height(node):
    if not node:
        return 0
    return node.height

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

if __name__ == '__main__':
    lst = list(map(int, input("values separated by space: ").split()))
    root = None
    for i in lst:
        root = bst(i, root)
    print("Inorder Traversal: ", end='')
    inorder_traversal(root)
    print()
    height = find_height(root)
    print("Height of the tree:", height)
