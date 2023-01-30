def same_type(fn):
    def wrapper(*args):
        types = set(map(type, args))
        if len(types) == 1:
            return fn(*args)
        else:
            return "Обнаружены различные типы данных\nFail"
    return wrapper