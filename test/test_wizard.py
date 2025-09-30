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
    test_wizard.drink(healing)
    assert test_wizard.mana == 150

