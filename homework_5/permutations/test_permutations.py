import io
import unittest
from contextlib import redirect_stdout
from permutations import permutations


class TestPermutations(unittest.TestCase):
    def check(self, nums, expected):
        original = nums.copy()
        with redirect_stdout(io.StringIO()):
            result = permutations(nums)
        self.assertCountEqual(result, expected)
        self.assertEqual(nums, original)  

    def test_examples(self):
        cases = [
            ([1], [[1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            (
                [1, 2, 3],
                [
                    [1, 2, 3], [1, 3, 2],
                    [2, 1, 3], [2, 3, 1],
                    [3, 1, 2], [3, 2, 1],
                ],
            ),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.check(nums, expected)

    def test_empty(self):
        self.check([], [[]])

    def test_negative_values(self):
        self.check(
            [-1, 0, 2],
            [
                [-1, 0, 2], [-1, 2, 0],
                [0, -1, 2], [0, 2, -1],
                [2, -1, 0], [2, 0, -1],
            ],
        )

    def test_four_elements(self):
        nums = [1, 2, 3, 4]
        with redirect_stdout(io.StringIO()):
            result = permutations(nums)
        self.assertEqual(len(result), 24)  
        self.assertEqual(len({tuple(p) for p in result}), 24)
        for permutation in result:
            self.assertCountEqual(permutation, nums)
