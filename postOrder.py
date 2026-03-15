def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)