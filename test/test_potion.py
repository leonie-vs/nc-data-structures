from src.potion import Potion

# Test 1 
def test_potion_attributes():
    healing = Potion("Healing Potion", "Green", 50)

    assert healing.name == "Healing Potion"
    assert healing.colour == "Green"
    assert healing.power_level == 50

# Testing methods to strengthen and weaken power_level
# Test 2 - strengthen increases value of power_level by correct amount
def test_strengthen_increases_power():
    p = Potion("Mana Potion", "Blue", 30)
    p.strengthen(15)
    assert p.power_level == 45

# Test 3 - weaken decreases value of power_level by correct amount
def test_weaken_decreases_power():
    p = Potion("Stamina Potion", "Red", 40)
    p.weaken(10)
    assert p.power_level == 30

# Test 4 - if amount to weaken is bigger than power_level, the value of power_level won't go past 0
def test_weaken_does_not_go_below_zero():
    p = Potion("Tiny Potion", "Purple", 5)
    p.weaken(10)
    assert p.power_level == 0

# Testing __str__ method
# Test 5 - using str(<potion>) returns string with object's actual name, colour, and power_level value
def test_str_returns_string_describing_object():
    healing = Potion("Healing Potion", "Green", 50)
    assert str(healing) == "Potion: Healing Potion (Green), Power Level: 50"
