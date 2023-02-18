def func(a, b, c):
    return ''.join(map(str, (a, b, c)))

class Except(Exception):
    def __str__(self):
        raise NameError
    def __repr__(self):
        raise NameError

try:
    func(Except(), 2, 3)
except NameError:
    print("Ура! Ошибка!")
except Exception:
    print("Ура! Ошибка!")