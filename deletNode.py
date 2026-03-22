class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert function
def insert(root, value):
    if root is None:
        return Node(value)
    
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

# Search function
def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Inorder Traversal (sorted output)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# ----------- Main Program -----------

root = None
values = [10, 5, 20, 3, 7, 30]

for v in values:
    root = insert(root, v)

print("Inorder Traversal:")
inorder(root)

print("\nSearch 7:", search(root, 7))
print("Search 15:", search(root, 15))