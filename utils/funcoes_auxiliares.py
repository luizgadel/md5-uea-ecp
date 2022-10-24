
def fun_aux(X, Y, Z):
    saida = ""
    for x, y, z in zip(X, Y, Z):
        if (x == '1'):
            saida += y
        else:
            saida += z

    return saida


def fun_aux_F(X, Y, Z):
    return fun_aux(X, Y, Z)


def fun_aux_G(X, Y, Z):
    return fun_aux(Z, X, Y)


def fun_aux_H(X, Y, Z):
    saida = ""
    for x, y, z in zip(X, Y, Z):
        if (x == '1'):
            saida += (y == z)
        else:
            saida += (y != z)

    return saida


def fun_aux_I(X, Y, Z):
    saida = ""
    for x, y, z in zip(X, Y, Z):
        if (z == '1'):
            saida += (x != y)
        else:
            saida += (x == '0')

    return saida
