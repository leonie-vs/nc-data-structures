from src.potion import Potion 
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