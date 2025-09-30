class Potion:
    def __init__(self, name, colour, power_level):
        self.name = name
        self.colour = colour
        self.power_level = power_level
    
    def describe(self):
        print(f'The {self.name} is {self.colour} with power level {self.power_level}.')
    
