def cycle(iterable):
    while iterable:
        for element in iterable:
            yield element


print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
