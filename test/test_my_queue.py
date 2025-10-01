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

# Test 5
def test_enqueue_adds_items_to_storage_until_storage_full():
    test_queue = Queue(max_size=2)
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    test_queue.enqueue("item3")
    assert len(test_queue.storage) == 2
    
# Test 6
def test_back_returns_item_most_recently_added_to_queue():
    test_queue = Queue()
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    test_queue.enqueue("item3")
    assert test_queue.back == "item3"
    assert test_queue.back == test_queue.storage[-1]

# Test 7 
def test_front_and_back_return_same_item_if_only_one_in_storage():
    test_queue = Queue()
    test_queue.enqueue("item1")
    assert test_queue.back == test_queue.front

# Test 8
def test_front_returns_item_at_front_of_queue():
    test_queue = Queue()
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    test_queue.enqueue("item3")
    assert test_queue.front == "item1"
    assert test_queue.front == test_queue.storage[0]

# Test 9 
def test_dequeue_cannot_remove_item_from_empty_queue():
    test_queue = Queue()
    assert test_queue.dequeue() == None
    assert len(test_queue.storage) == 0

# Test 10
def test_dequeue_removes_one_item_from_queue_until_empty():
    test_queue = Queue()
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    test_queue.dequeue()
    assert len(test_queue.storage) == 1
    test_queue.dequeue()
    assert len(test_queue.storage) == 0

# Test 11
def test_dequeue_removes_from_zero_index_of_storage():
    test_queue = Queue()
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    test_queue.dequeue()
    assert test_queue.storage == ["item2"]

# Test 12
def test_enqueue_updates_front_and_back_correctly():
    test_queue = Queue()
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    test_queue.enqueue("item3")
    test_queue.dequeue()
    assert test_queue.front == "item2"
    assert test_queue.back == "item3"

# Test 13
def test_dequeue_returns_removed_item_correctly():
    test_queue = Queue()
    test_queue.enqueue("item1")
    test_queue.enqueue("item2")
    assert test_queue.dequeue() == "item1"
    assert test_queue.dequeue() == "item2"
    assert test_queue.dequeue() == None

# Test 14
def test_get_quantity_method_returns_current_length_of_storage_list():
    test_queue = Queue()
    assert test_queue.get_quantity() == 0
    test_queue.enqueue("item1")
    assert test_queue.get_quantity() == 1
    test_queue.enqueue("item2")
    assert test_queue.get_quantity() == 2
    test_queue.dequeue()
    assert test_queue.get_quantity() == 1









    
