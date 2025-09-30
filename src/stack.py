class Stack:
    def __init__(self, max_size=10):
        self.quantity = 0
        self.storage = {}
        self.max_size = max_size
    
    def push(self, item):
        if self.quantity >= self.max_size:
            print(f"Stack is full")
            return
        self.storage[self.quantity] = item
        self.quantity += 1
    
    def pop(self):
        if self.quantity == 0:
            print("Stack is empty")
            return
        self.quantity -= 1
        return self.storage.pop(self.quantity)
    
    def is_empty(self):
        if self.quantity == 0 and self.storage == {}:
            return True
        return False

        
