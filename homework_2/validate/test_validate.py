from validate import valid

def run_tests():
    assert valid([1], [1]) == True
    assert valid([1, 2], [1, 2]) == True
    assert valid([1, 2], [2, 1]) == True
    assert valid([1, 2, 3], [3, 2, 1]) == True
    assert valid([1, 2, 3], [1, 2, 3]) == True
    assert valid([1, 2, 3], [3, 1, 2]) == False
    assert valid(
        [1, 2, 3, 4, 5],
        [1, 3, 5, 4, 2]
    ) == True
    assert valid(
        [1, 2, 3, 4, 5],
        [4, 5, 3, 2, 1]
    ) == True
    assert valid(
        [1, 2, 3, 4, 5],
        [4, 3, 5, 1, 2]
    ) == False
    assert valid(
        [1, 2, 3, 4],
        [2, 1, 4, 3]
    ) == True
    assert valid(
        [1, 2, 3, 4],
        [2, 4, 1, 3]
    ) == False
    assert valid(
        [10, 20, 30, 40],
        [30, 40, 20, 10]
    ) == True
    assert valid(
        [1, 2, 3, 4, 5, 6],
        [2, 1, 4, 3, 6, 5]
    ) == True
    assert valid(
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1, 6, 5, 4]
    ) == True
    assert valid(
        [1, 2, 3, 4, 5, 6],
        [3, 1, 2, 6, 5, 4]
    ) == False
    print("Ок")

run_tests()