class Set:
    def __init__(self, set=None):
        if set is None:
            self.set = []
        else:
            self.set = []
            for item in set:
                if item not in self.set:
                    self.set.append(item)
    
    def add(self, item):
        if item not in self.set:
            self.set.append(item)
            return
        return print(f'No duplicates allowed')


    
        
        

    
