def converteIntParaBinario(x, tam_final):
    x_em_binario = bin(x)[2:]
    if (len(x_em_binario) < tam_final):
        x_em_binario = x_em_binario.rjust(tam_final, '0')
    else:
        x_em_binario = x_em_binario[-tam_final:]
    return x_em_binario


def desloca_esquerda(x: int, n: int, mod=32):
    pot_max: int = 2**mod
    resultado = x << n
    overflow = resultado // pot_max
    resultado = resultado % pot_max + overflow
    return resultado
