def func(a, b):
    return a + b

try:
    func(None, 0)
except TypeError:
    print("Ура! Ошибка!")
except Exception:
    print("Ура! Ошибка!")