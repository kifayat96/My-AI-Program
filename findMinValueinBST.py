def find_max(root):
    while root.right:
        root = root.right
    return root.data

print(find_max(root))