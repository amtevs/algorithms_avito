from iterative import mergesort_iterative, quicksort_iterative

cases = [
    [],
    [1],
    [2, 1],
    [4, 1, 3, 2],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [5, 5, 5],
    [0, -2, 3, -2, 1],
]
for nums in cases:
    original = nums[:]
    assert mergesort_iterative(nums) == sorted(nums)
    assert quicksort_iterative(nums) == sorted(nums)
    assert nums == original
print("Все ок")