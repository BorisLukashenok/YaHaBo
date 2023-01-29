from itertools import cycle
def secret_replace(stroka, **args):
    gen = {}
    for key in args.keys():
        gen[key] = cycle(args[key])
    out = ''
    for i in stroka:
        if i in gen.keys():
            out += next(gen[i])
        else:
            out += i            
    return out


print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))
print(secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
))