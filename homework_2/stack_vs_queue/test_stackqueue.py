from stack_vs_queue import Mystack, MyQueue


def test_stack_empty():
    stack = Mystack()
    assert stack.empty() is True
    assert stack.peek() is None
    assert stack.pop() is None


def test_stack_push_one():
    stack = Mystack()
    stack.push(10)
    assert stack.empty() is False
    assert stack.peek() == 10


def test_stack_lifo():
    stack = Mystack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.empty() is True


def test_stack_push_after_pop():
    stack = Mystack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 1
    assert stack.empty() is True


def test_stack_many_elements():
    stack = Mystack()
    for i in range(100):
        stack.push(i)
    for i in range(99, -1, -1):
        assert stack.pop() == i
    assert stack.empty() is True


def test_queue_empty():
    queue = MyQueue()
    assert queue.empty() is True
    assert queue.dequeue() is None


def test_queue_enqueue_one():
    queue = MyQueue()
    queue.enqueue(10)
    assert queue.empty() is False
    assert queue.dequeue() == 10
    assert queue.empty() is True


def test_queue_fifo():
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.empty() is True


def test_queue_enqueue_after_dequeue():
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.empty() is True


def test_queue_reuse_after_empty():
    queue = MyQueue()
    queue.enqueue(1)
    assert queue.dequeue() == 1
    assert queue.empty() is True
    queue.enqueue(2)
    assert queue.empty() is False
    assert queue.dequeue() == 2
    assert queue.empty() is True


def test_queue_many_elements():
    queue = MyQueue()
    for i in range(100):
        queue.enqueue(i)
    for i in range(100):
        assert queue.dequeue() == i
    assert queue.empty() is True
    
    
def run_tests():
    test_stack_empty()
    test_stack_push_one()
    test_stack_lifo()
    test_stack_push_after_pop()
    test_stack_many_elements()

    test_queue_empty()
    test_queue_enqueue_one()
    test_queue_fifo()
    test_queue_enqueue_after_dequeue()
    test_queue_reuse_after_empty()
    test_queue_many_elements()

    print("ок")


if __name__ == "__main__":
    run_tests()