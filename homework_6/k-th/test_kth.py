from kth import kth_largest

def test_kth_largest():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([7], 1) == 7
    assert kth_largest([2, 8, 4], 1) == 8   
    assert kth_largest([2, 8, 4], 3) == 2   
    assert kth_largest([5, 5, 5], 2) == 5
    assert kth_largest([-3, -1, -2], 2) == -2
    print("Все ок")
