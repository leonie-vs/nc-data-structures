class Queue:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.storage = []
        self.front = None
        self.back = None
