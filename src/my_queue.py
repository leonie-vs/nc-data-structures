class Queue:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.storage = []
        self.front = None
        self.back = None
    
    def enqueue(self, item):
        if len(self.storage) >= self.max_size:
            print("Queue is full")
            return 
        self.storage.append(item)
        self.back = item
        self.front = self.storage[0]
    
    def dequeue(self):
        if len(self.storage) == 0:
            print("Queue is empty")
            return
        removed_item = self.storage.pop(0)
        if len(self.storage) == 0:
             self.back = None
             self.front = None
        else:
            self.back = self.storage[-1]
            self.front = self.storage[0]
        return removed_item
    
    def get_quantity(self):
        return len(self.storage)
    
    def is_empty(self):
        return self.get_quantity() == 0
    
    def is_full(self):
        if self.get_quantity() == self.max_size:
            return True
        return False
    
    

        
        
    
    

            
        


