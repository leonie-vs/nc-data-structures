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

# Try push method and max_size
test_stack = Stack(max_size=2)
test_stack.push('apple')
print(test_stack.storage)  
print(test_stack.quantity) 
test_stack.push('banana')
print(test_stack.storage) 
print(test_stack.quantity) 
test_stack.push('cherry')  
print(test_stack.quantity)

# Try is_empty method
empty_stack = Stack()
print(empty_stack.is_empty())

empty_stack.push('cherry')
print(empty_stack.is_empty())

# Try is_full method
full_stack = Stack(max_size=2)
full_stack.push('apple')
full_stack.push('cherry')
print(full_stack.is_full()) 
full_stack.pop()
print(full_stack.is_full()) 
full_stack.push('banana')
print(full_stack.is_full()) 
print(full_stack.quantity) 

# Try peek method
test_stack = Stack()
test_stack.push('apple')
test_stack.push('orange')
test_stack.push('banana')
test_stack.push('kiwi')
test_stack.push('pear')
print(test_stack.storage) # {0: 'apple', 1: 'orange', 2: 'banana', 3: 'kiwi', 4: 'pear'}
print(test_stack.peek) # returns 'pear'
test_stack.pop()
print(test_stack.peek)  # returns 'kiwi'




from src.my_queue import Queue

# Try adjusting max_size instead of having a default value and print it
test_queue = Queue(max_size=5)
print(test_queue.max_size) # 5




from src.my_set import Set

set_1 = Set([1, 2])
set_2 = Set([2, 3])

# Union: items from both sets, no duplicates
print(set_1.union(set_2))       # -> {1, 2, 3}

# Intersection: items common to both sets
print(set_1.intersection(set_2))  # -> {2}

# Difference: items in set_1 but not in set_2
print(set_1.difference(set_2))  # -> {1}
