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

def mergesort_iterative(nums):
    a = nums[:]
    n = len(a)
    w = 1
    while w < n:
        for start in range(0, n, 2 * w):
            mid = min(start + w, n)
            end = min(start + 2 * w, n)
            left = a[start:mid]
            right = a[mid:end]
            a[start:end] = merge(left, right)
        w *= 2
    return a


def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i

def quicksort_iterative(nums):
    a = nums[:]
    stack = [(0, len(a) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        p = partition(a, low, high)
        if low < p - 1:
            stack.append((low, p - 1))
        if p + 1 < high:
            stack.append((p + 1, high))
    return a