data_first = []
data_second = []


def enter_results(*args):
    for i in range(0, len(args), 2):
        a, b = args[i: i + 2]
        data_first.append(a)
        data_second.append(b)


def get_sum():
    return round(sum(data_first), 2), round(sum(data_second), 2)


def get_average():
    a, b = get_sum()
    return round(a / len(data_first), 2), round(b / len(data_second), 2)


enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
