def prime(n: int):
    if n <= 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p < n:
        if is_prime[p]:
            for m in range(p * p, n, p):
                is_prime[m] = False
        p += 1
    return sum(is_prime)
