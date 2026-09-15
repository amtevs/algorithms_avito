import pytest
from prime import prime

@pytest.mark.parametrize(
    "n,expected",
    [
        (10, 4),  
        (1, 0),  

        (0, 0),    
        (2, 0),   
        (3, 1),    
        (4, 2),
        (-5, 0),    

        (7, 3),   
        (8, 4),    
        (11, 4),   
        
        (100, 25),
        (101, 25), 
    ],
)
def test_count_primes_basic(n, expected):
    assert prime(n) == expected


