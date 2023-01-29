def merge(t1, t2):
    return tuple(sorted(t1 + t2))


print(merge((1, 2), (3, 4, 5)))
print(merge((7, 12), (1, 9, 50)))