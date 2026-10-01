def anagrams(strs):
    d = {}
    for i in strs:
        s = ''.join(sorted(i))
        if s not in d:
            d[s] = []
        d[s].append(i)
    return list(d.values())