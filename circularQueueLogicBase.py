class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.size = size
        self.front = self.rear = -1