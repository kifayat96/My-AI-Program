def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)