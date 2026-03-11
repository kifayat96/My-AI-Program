def insert_begin(self, data):
    new_node = Node(data)

    if self.head is not None:
        self.head.prev = new_node
        new_node.next = self.head

    self.head = new_node