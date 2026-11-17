from random import random
from compare import mergesort, quicksort


def test_sorting():
    cases = [
        [],                   
        [1],                 
        [2, 1],              
        [1, 2, 3, 4],         
        [4, 3, 2, 1],        
        [5, 5, 5],           
        [3, -1, 0, 3, -5],   
    ]
    for nums in cases:
        original = nums[:]
        expected = sorted(nums)
        assert mergesort(nums) == expected
        assert quicksort(nums) == expected
        assert nums == original
    print("Все ок")

def compare_time():
    n = 500
    rng = random.Random(42)
    cases = {
        "Случайный порядок": rng.sample(range(n), n),
        "По возрастанию": list(range(n)),
        "По убыванию": list(range(n - 1, -1, -1)),
        "Все элементы одинаковые": [7] * n,
    }
    for name, nums in cases.items():
        print(f"\n{name}, размер {n}")
        for repeat in range(3):
            print(f"Запуск {repeat + 1}")
            assert mergesort(nums) == sorted(nums)
            assert quicksort(nums) == sorted(nums)
