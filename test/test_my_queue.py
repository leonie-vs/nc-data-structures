from src.my_queue import Queue

# Test 1
def test_max_size_attribute_returns_default_value_or_value_passed_as_argument():
    test_queue = Queue()
    assert test_queue.max_size == 10
    test_queue = Queue(max_size=5)
    assert test_queue.max_size == 5

# Test 2
def test_storage_attribute_is_initially_empty_list():
    test_queue = Queue()
    assert test_queue.storage == []
    assert type(test_queue.storage) == list

# Test 3
def test_front_returns_none_if_queue_empty():
    test_queue = Queue()
    assert test_queue.front == None

# Test 4
def test_back_returns_none_if_queue_empty():
    test_queue = Queue()
    assert test_queue.back == None

    
