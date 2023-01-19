def vz_prost(a, b):
    while b:
        a, b = b, a % b
    return not a + b - 1


s = sorted(map(int, set(input().split('; '))))
print('\n'.join(
    [f'{i} - {", ".join(map(str, [j for j in s if vz_prost(i, j)]))}' for i in s if any([vz_prost(i, j) for j in s])]))
