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
