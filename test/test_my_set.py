from src.my_set import Set
from src.potion import Potion

## Set attributes:
# an instance of a set is an unordered collection of items
# an instance of a set doesn't allow duplicate items 

## Set methods:
# add
# remove
# union
# intersection
# difference

# Test 1
def test_set_is_empty_list_if_no_argument_passed():
    test_set = Set()
    assert test_set.set == []

# Test 2
def test_set_only_allows_unique_items_to_be_added():
    test_set = Set([1, 2, 3, 2])
    assert test_set.set == [1, 2, 3]

# Test 3
def test_add_method_cannot_add_duplicates_to_set():
    test_set = Set([1, 2, 3])
    test_set.add(2)
    assert test_set.set == [1, 2, 3]

# Test 4
def test_add_method_adds_non_duplicate_items_to_set():
    test_set = Set([1, 2, 3])
    test_set.add(4)
    assert test_set.set == [1, 2, 3, 4]

# Test 5
def test_remove_method_cannot_remove_nonexisting_item():
    test_set = Set([1, 2, 3])
    assert test_set.remove(4) == 'KeyError: 4'
    assert test_set.set == [1, 2, 3]

# Test 6 
def test_remove_method_removes_existing_item():
    test_set = Set(["hello", "bye", 3])
    test_set.remove("hello") 
    assert test_set.set == ["bye", 3]

# Test 7 
def test_union_method_combines_items_of_two_lists_into_one_new_list():
    test_set = Set([1, 2, 3])
    test_list = ['hello', 'bye']
    assert test_set.union(test_list) == [1, 2, 3, 'hello', 'bye']
    assert test_set.set == [1, 2, 3]

# Test 8
def test_intersection_method_returns_new_list_with_shared_elements():
    test_set = Set([1, 2, 3])
    test_list = [1, 3, 4, 5]
    assert test_set.intersection(test_list) == [1, 3]
    assert test_set.set == [1, 2, 3]

# Test 9
def test_difference_method_returns_new_list_with_elements_from_set_that_are_not_in_list():
    test_set = Set([1, 2, 2, 3, 6])
    test_list = [1, 2, 3, 4, 5]
    assert test_set.difference(test_list) == [6]
    assert test_set.set == [1, 2, 3, 6]
 
 # Test 10 
def test_set_instances_are_iterable():
    test_set1 = Set([1, 2, 2, 3, 6])
    test_set2 = Set([1, 2, 3, 4, 5])
    assert test_set1.difference(test_set2) == [6]
    assert test_set1.set == [1, 2, 3, 6]

# Test 11
def test_set_works_with_instances_of_a_class():
    healing = Potion("Healing Potion", "Green", 30)
    stamina = Potion("Stamina Potion", "Blue", 30)
    speed = Potion("Speed Potion", "Yellow", 10)
    test_set1 = Set([healing, stamina])
    test_set2 = Set([speed])
    assert test_set1.union(test_set2) == [healing, stamina, speed]
    test_set1.add(stamina)
    test_set1.add(speed)
    assert test_set1.set == [healing, stamina, speed]



