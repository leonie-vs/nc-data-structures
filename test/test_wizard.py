from src.wizard import Wizard
from src.potion import Potion

# Test 1
def test_wizard_contains_name_attribute():
    test_wizard = Wizard("Merlin")
    assert test_wizard.name == "Merlin"

# Test 2
def test_wizard_contains_mana_attribute_with_default_100():
    test_wizard = Wizard("Merlin")
    assert test_wizard.mana == 100

# Test 3
def test_drink_method_increases_mana_by_correct_amount():
    test_wizard = Wizard("Merlin")
    healing = Potion("Healing Potion", "Green", 50)
    test_wizard.add_potion(healing)
    test_wizard.drink(healing)
    assert test_wizard.mana == 150

# Test 4
def test_wizard_has_inventory_attribute_that_starts_empty():
    test_wizard = Wizard("Merlin")
    assert test_wizard.inventory == [] 

# Test 5
def test_add_potion_method_adds_potion_to_inventory_list():
    test_wizard = Wizard("Merlin")
    healing = Potion("Healing Potion", "Green", 50)
    test_wizard.add_potion(healing)

    assert test_wizard.inventory == [healing]

# Test 6 
def test_cannot_drink_potion_if_not_in_inventory():
    test_wizard = Wizard("Merlin")
    healing = Potion("Healing Potion", "Green", 50)
    stamina = Potion("Stamina Potion", "Red", 60)
    
    test_wizard.add_potion(healing)
    
    result = test_wizard.drink(stamina)

    assert result == False

# Test 7
def test_potion_removed_from_inventory_after_drink_method():
    test_wizard = Wizard("Merlin")
    healing = Potion("Healing Potion", "Green", 50)
    
    test_wizard.add_potion(healing)
    
    assert test_wizard.inventory == [healing]

    test_wizard.drink(healing)

    assert test_wizard.inventory == []

    



