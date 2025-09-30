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
