from src.stack import Stack

# Test 1 
def test_quantity_initially_zero():
    test_stack = Stack()
    assert test_stack.quantity == 0

# Test 2
def test_storage_initially_empty():
    test_stack = Stack()
    assert test_stack.storage == {}

# Test 3
def test_properties_type():
    test_stack = Stack()
    assert isinstance(test_stack.quantity, int)
    assert isinstance(test_stack.storage, dict)

# Test 4
def test_stack_max_size_default_when_not_specified_in_argument():
    test_stack = Stack()
    assert test_stack.max_size == 10  

# Test 5
def test_stack_max_size_custom():
    test_stack = Stack(5)
    assert test_stack.max_size == 5

# Test 6
def test_push_increases_quantity_by_one_for_each_item():
    test_stack = Stack()
    item1 = "apple"
    item2 = "banana"
    
    test_stack.push(item1)
    assert test_stack.quantity == 1

    test_stack.push(item2)
    assert test_stack.quantity == 2
    
# Test 7 
def test_pushed_item_added_to_storage():
    test_stack = Stack()
    item1 = "apple"
    item2 = "banana"
    
    test_stack.push(item1)
    assert test_stack.storage == {0: "apple"}

    test_stack.push(item2)
    assert test_stack.storage == {0: "apple", 1: "banana"}

# Test 8
def test_push_respects_max_size():
    test_stack = Stack(max_size=1)
    test_stack.push('apple')
    test_stack.push('banana') 
    assert test_stack.quantity == 1

# Test 9
def test_pop_removes_and_returns_item_at_highest_index_in_storage():
    test_stack = Stack()  
    test_stack.push("apple")
    test_stack.push("banana")

    assert test_stack.pop() == "banana"
    assert test_stack.quantity == 1

# Test 10
def test_pop_handles_empty_storage_without_error():
    test_stack = Stack()  
    test_stack.push("apple")
    test_stack.push("banana")

    test_stack.pop()
    test_stack.pop()

    assert test_stack.pop() == None
    assert test_stack.quantity == 0
    assert test_stack.storage == {}

# Test 11
def test_is_empty_returns_boolean_correctly():
    test_stack = Stack()
    assert test_stack.is_empty() == True

    test_stack.push("apple")
    test_stack.push("banana")
    assert test_stack.is_empty() == False

# Test 12
def test_is_full_returns_true_when_stack_full():
    test_stack = Stack(max_size=2)
    assert test_stack.is_full() == False

    test_stack.push("apple")
    test_stack.push("banana")
    assert test_stack.is_full() == True

# Test 13
def test_is_full_returns_false_when_previously_full_stack_becomes_empty():
    test_stack = Stack(max_size=2)
    test_stack.push("apple")
    test_stack.push("cherry")
    assert test_stack.is_full() == True
    test_stack.pop()
    assert test_stack.is_full() == False

# Test 14
def test_peek_returns_none_when_stack_empty():
    test_stack = Stack()
    assert test_stack.peek == None

# Test 15
def test_peek_returns_most_recently_added_item():
    test_stack = Stack()
    test_stack.push("apple")
    test_stack.push("cherry")
    assert test_stack.peek == "cherry"

# Test 16
def test_peek_returns_item_without_removing_it():
    test_stack = Stack()
    test_stack.push("apple")
    test_stack.push("cherry")
    test_stack.peek
    assert test_stack.storage[test_stack.quantity - 1] == "cherry"



