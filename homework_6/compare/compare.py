from time import perf_counter
from functools import wraps
import random


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{func.__name__}: {elapsed:.6f} с")
        return result

    return wrapper

def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

@measure_time
def mergesort(nums):
    def sort(a):
        if len(a) <= 1:
            return a[:]
        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])
        return merge(left, right)

    return sort(nums)


def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i


@measure_time
def quicksort(nums):
    a = nums[:]
    def sort(low, high):
        if low >= high:
            return
        p = partition(a, low, high)
        sort(low, p - 1)
        sort(p + 1, high)
        
    sort(0, len(a) - 1)
    return a