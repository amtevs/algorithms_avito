def palindrom(a: int):
    n = a
    k = 0
    while n != 0:
        n = n // 10
        k += 1
    for i in range(k // 2):
        if ((a // 10**(i)) % 10) != ((a // 10**(k-i-1)) % 10):
            return False
    return True