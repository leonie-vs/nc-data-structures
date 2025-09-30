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
def test_push_respects_max_size(capsys):
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
   