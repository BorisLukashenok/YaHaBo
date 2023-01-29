def to_string(*args, sep=" ", end="\n"):
    return sep.join([str(arg) for arg in args]) + end