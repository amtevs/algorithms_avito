def valid(pushed, popped):
    res = []
    j = 0
    for x in pushed:
        res.append(x)
        while res and j < len(popped) and res[-1] == popped[j]:
            res.pop()
            j += 1
    return j == len(popped)
    