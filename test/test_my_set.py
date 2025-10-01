from src.my_set import Set

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



