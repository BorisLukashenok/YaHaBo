def make_linear(lst):
    out = []
    for i in lst:
        if isinstance(i, list):
            out.extend(make_linear(i))
        else:
            out.append(i)
    return out


print(make_linear([1, [2, [3, 4]], 5, 6]))
