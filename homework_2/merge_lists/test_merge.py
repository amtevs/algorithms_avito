from merge_lists import merge_with_dummy, merge_without_dummy, ListNode

def make_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    cur = head

    for value in values[1:]:
        cur.next = ListNode(value)
        cur = cur.next

    return head


def to_list(head):
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    return result
    
    
def test_merge_with_dummy():
    list1 = make_list([1, 2, 4])
    list2 = make_list([1, 3, 4])

    result = merge_with_dummy(list1, list2)

    assert to_list(result) == [1, 1, 2, 3, 4, 4]


def test_merge_without_dummy():
    list1 = make_list([1, 2, 4])
    list2 = make_list([1, 3, 4])

    result = merge_without_dummy(list1, list2)

    assert to_list(result) == [1, 1, 2, 3, 4, 4]


def test_first_empty():
    assert to_list(
        merge_with_dummy(None, make_list([1, 2, 3]))
    ) == [1, 2, 3]

    assert to_list(
        merge_without_dummy(None, make_list([1, 2, 3]))
    ) == [1, 2, 3]


def test_second_empty():
    assert to_list(
        merge_with_dummy(make_list([1, 2, 3]), None)
    ) == [1, 2, 3]

    assert to_list(
        merge_without_dummy(make_list([1, 2, 3]), None)
    ) == [1, 2, 3]


def test_both_empty():
    assert merge_with_dummy(None, None) is None
    assert merge_without_dummy(None, None) is None


def test_different_lengths():
    list1 = make_list([1, 5])
    list2 = make_list([2, 3, 4, 6, 7])

    result = merge_with_dummy(list1, list2)

    assert to_list(result) == [1, 2, 3, 4, 5, 6, 7]
    
def run_tests():
    test_merge_with_dummy()
    test_merge_without_dummy()
    test_first_empty()
    test_second_empty()
    test_both_empty()
    test_different_lengths()

    print("ок")
    
    
if __name__ == "__main__":
    run_tests()
    