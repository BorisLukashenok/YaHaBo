def only_positive_even_sum(a, b):
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError
        if not (a > 0 and a % 2 == 0) or not (b > 0 and b % 2 == 0):
            raise ValueError
    except TypeError:
        return "Вызвано исключение TypeError"
    except ValueError:
        return "Вызвано исключение ValueError"
    return a + b