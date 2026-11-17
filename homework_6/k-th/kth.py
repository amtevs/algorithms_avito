def partition(a, low, high):
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i

def kth_largest(nums, k):
    a = nums[:]
    target = len(a) - k
    low = 0
    high = len(a) - 1
    while low <= high:
        p = partition(a, low, high)
        if p == target:
            return a[p]
        elif p < target:
            low = p + 1
        else:
            high = p - 1