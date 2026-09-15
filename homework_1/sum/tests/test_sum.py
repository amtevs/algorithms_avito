import pytest
from max_sum import max_sum

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([5, 7, 13, 2, 14], 36),  
        ([3], 0),                  
        
        ([2, 4, 6], 12),          
        ([10], 10),         

        ([1, 3, 5], 8),          
        ([7], 0),                
        ([1, 1, 1], 2),       

        ([1, 2], 2),             
        ([1, 2, 3], 6),   
        
        ([], 0),

        ([1000000, 1000001], 1000000), 
        ([999999, 999998], 999998),   
    ],
)
def test_max_even_sum_basic(nums, expected):
    assert max_sum(nums) == expected