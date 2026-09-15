from typing import List

def max_sum(nums: List[int]):
    m = None
    s = 0
    for i in nums:
        s += i
        if i % 2 != 0:
            if m is None or i < m:
                m = i
    if m is None:
        m = 0
    if s % 2 == 0:
        return s
    else:
        return s - m