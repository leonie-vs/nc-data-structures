from src.potion import Potion

# Test 1
def test_potion_attributes():
    healing = Potion("Healing Potion", "Green", 50)

    assert healing.name == "Healing Potion"
    assert healing.colour == "Green"
    assert healing.power_level == 50