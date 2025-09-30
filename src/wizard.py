from src.potion import Potion

class Wizard:
    def __init__(self, name, mana=100, inventory=None):
        self.name = name
        self.mana = mana
        self.inventory = [] if inventory is None else inventory
    
    def drink(self, potion: Potion):
        if potion in self.inventory:
            self.mana += potion.power_level
            self.inventory.remove(potion)
            print(f'{self.name} drinks {potion.name}! His mana increases by {potion.power_level}.')
        else:
            print(f"{self.name} cannot drink potions that are not in the inventory")
            return False

    def add_potion(self, potion):
        self.inventory.append(potion) 
    
    def inventory_contents(self):
        if not self.inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            potion_names = [potion.name for potion in self.inventory]
            print(f"{self.name}'s Inventory: {potion_names}")


    