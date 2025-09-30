class Potion:
    def __init__(self, name, colour, power_level):
        self.name = name
        self.colour = colour
        self.power_level = power_level
        
    def describe(self):
        print(f'The {self.name} is {self.colour} with power level {self.power_level}.')
    
    def strengthen(self, amount):
        self.power_level += amount
    
    def weaken(self, amount):
        if amount > self.power_level:
            self.power_level = 0
        else:
            self.power_level -= amount
    
    def __str__(self):
        return f'Potion: {self.name} ({self.colour}), Power Level: {self.power_level}'
    
    
