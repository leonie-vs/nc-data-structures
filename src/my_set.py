class Set:
    def __init__(self, set=None):
        if set is None:
            self.set = []
        else:
            self.set = []
            for item in set:
                if item not in self.set:
                    self.set.append(item)
    
    def __iter__(self):
        return iter((self.set))

    def add(self, item):
        if item not in self.set:
            self.set.append(item)
            return
        return print(f'No duplicates allowed')

    def remove(self, item):
        if item not in self.set:
            return f'KeyError: {item}'
        self.set.remove(item)
    
    def union(self, second_list):
        union_set = []
        union_set.extend(self.set)
        for item in second_list:
            if item not in union_set:
                union_set.append(item)
        return union_set
    
    def intersection(self, second_list):
        intersection_set = []
        for item in second_list:
            if item in self.set:
                intersection_set.append(item)
        return intersection_set

    def difference(self, second_list):
        difference_set = []
        for item in self.set:
            if item not in second_list:
                difference_set.append(item)
        return difference_set
        
    
    


    
        
        

    
