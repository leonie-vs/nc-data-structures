from src.potion import Potion

class Wizard:
    def __init__(self, name, mana=100):
        self.name = name
        self.mana = mana
    
    def drink(self, potion: Potion):
        self.mana += potion.power_level
        print(f'{self.name} drinks {potion.name}! His mana increases by {potion.power_level}.')

    