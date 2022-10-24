
from utils.int_utils import converteIntParaBinario, desloca_esquerda
from utils.string_utils import imprimeBinario


def fun_aux(X: int, Y: int, Z: int):
    x_bin = bin(X)[2:]
    y_bin = bin(Y)[2:]
    z_bin = bin(Z)[2:]
    saida = ""
    for x, y, z in zip(x_bin, y_bin, z_bin):
        if (x == '1'):
            saida += y
        else:
            saida += z

    saida_int = int(saida, base=2)
    return saida_int


def fun_aux_F(X: int, Y: int, Z: int):
    return fun_aux(X, Y, Z)


def fun_aux_G(X: int, Y: int, Z: int):
    return fun_aux(Z, X, Y)


def fun_aux_H(X: int, Y: int, Z: int):
    x_bin = bin(X)[2:]
    y_bin = bin(Y)[2:]
    z_bin = bin(Z)[2:]
    saida = ""
    for x, y, z in zip(x_bin, y_bin, z_bin):
        if (x == '1'):
            saida += '1' if (y == z) else '0'
        else:
            saida += '1' if (y != z) else '0'

    saida_int = int(saida, base=2)
    return saida_int


def fun_aux_I(X: int, Y: int, Z: int):
    x_bin = bin(X)[2:]
    y_bin = bin(Y)[2:]
    z_bin = bin(Z)[2:]
    saida = ""
    for x, y, z in zip(x_bin, y_bin, z_bin):
        if (z == '1'):
            saida += '1' if (x != y) else '0'
        else:
            saida += '1' if (x == '0') else '0'

    saida_int = int(saida, base=2)
    return saida_int


def fun_round(a: int, b: int, c: int, d: int, x: int, s: int, t: int, num_round: int):
    resultado_f_aux = ""
    if (num_round == 1):
        resultado_f_aux = fun_aux_F(b, c, d)
    elif (num_round == 2):
        resultado_f_aux = fun_aux_G(b, c, d)
    elif (num_round == 3):
        resultado_f_aux = fun_aux_H(b, c, d)
    else:
        resultado_f_aux = fun_aux_I(b, c, d)
    a += resultado_f_aux + x + t
    a = desloca_esquerda(a, s)
    a += b
    return a
