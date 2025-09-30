from src.potion import Potion 
from src.wizard import Wizard 

# Create different potions using Potion class
healing = Potion("Healing Potion", "Green", 50)
stamina = Potion("Stamina Potion", "Red", 60)
speed = Potion("Speed Potion", "Blue", 20)

# Describe the potions using the describe method 
healing.describe()
stamina.describe()
speed.describe()

# Weaken and strengthen the potions using the weaken and strengthen methods
stamina.strengthen(15)
print(stamina.power_level)
speed.weaken(5)
print(speed.power_level)
healing.weaken(60)
print(healing.power_level)

# Print the attributes of the potions using print()
print(healing)
print(stamina)
print(speed)


# Create a wizard using Wizard class
merlin = Wizard("Merlin")

# Print the wizard's mana before drinking potion
print(f'Mana before drinking a stamina potion: {merlin.mana}')
# Let wizard drink potion
merlin.drink(stamina)
# Print the wizard's mana after drinking potion
print(f'Mana after drinking a stamina potion: {merlin.mana}')


# Add potions to the inventory
merlin.add_potion(healing)
merlin.add_potion(stamina)
merlin.add_potion(speed)

# Print the wizard's inventory contents
merlin.inventory_contents()
# Drink potions from inventory
merlin.drink(healing)
merlin.drink(speed)
# Print inventory after drinking potions
merlin.inventory_contents()
# Drink last potion from inventory and print empty inventory contents
merlin.drink(stamina)
merlin.inventory_contents()



from src.stack import Stack

# Initialise stack and see default values
some_stack = Stack()
print(some_stack.quantity)
print(some_stack.storage)
print(some_stack.max_size)
