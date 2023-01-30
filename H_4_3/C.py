def make_equation(*coefs):
    if len(coefs) == 1:
        return str(coefs[0])
    else:
        return '(' + make_equation(*coefs[:-1]) + ') * x + ' + str(coefs[-1])