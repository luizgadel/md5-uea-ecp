def imprimeBinario(bin):
    if (len(bin) > 20):
        msg = f"{len(bin)} - {bin[:10]}...{bin[-10:]}"
    else:
        msg = f"{len(bin)} - {bin}"

    print(msg)


def converteStrParaBinario(msg):
    bin_msg = ""
    for caractere in msg:
        bin_msg += bin(ord(caractere))[2:]
    return bin_msg


def extensao_passo_1(msg_binaria):
    congruent = 448
    modulo = 512

    msg_estendida = (msg_binaria + '1')

    tam_atual_msg = len(msg_estendida)
    if (tam_atual_msg >= congruent):
        tam_final = ((tam_atual_msg - congruent) //
                     modulo + 1) * modulo + congruent
    else:
        tam_final = congruent

    msg_estendida = msg_estendida.ljust(tam_final, '0')
    return msg_estendida


def converteIntParaBinario(x, tam_final):
    x_em_binario = bin(x)[2:]
    if (len(x_em_binario) < tam_final):
        x_em_binario = x_em_binario.rjust(tam_final, '0')
    else:
        x_em_binario = x_em_binario[-tam_final:]
    return x_em_binario


def extensao_passo_2(msg_passo_1, b):
    b_64bit = converteIntParaBinario(b, 64)
    return msg_passo_1 + b_64bit


def string_reversa(str):
    return str[::-1]


def inicializa_md_buffer():
    MD_buffer_hex = {
        "A": "01234567",
        "B": "89abcdef",
        "C": "fedcba98",
        "D": "76543210"
    }
    MD_buffer = {}
    tam_nibble = 4
    for w in MD_buffer_hex:
        nibble_bin = ""
        for nibble_hex in MD_buffer_hex[w]:
            nibble_bin += string_reversa(bin(int(nibble_hex, base=16))
                                         [2:].zfill(tam_nibble))
        MD_buffer[w] = nibble_bin

    return MD_buffer


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


mensagem = input("Digite a mensagem:")
tam_msg_original = len(mensagem)
msg_binaria = converteStrParaBinario(mensagem)
imprimeBinario(msg_binaria)

print("\nPasso 1: Extensão com bits de preenchimento")
msg_passo_1 = extensao_passo_1(msg_binaria)
imprimeBinario(msg_passo_1)

print("\nPasso 2: Extensão com o valor do tamanho")
msg_passo_2 = extensao_passo_2(msg_passo_1, tam_msg_original)
imprimeBinario(msg_passo_2)

print("\nPasso 3: Inicializar Buffer MD")
MD_buffer = inicializa_md_buffer()
print(MD_buffer)

print("\nPasso 4: Processamento da mensagem em blocos de 16 palavras")
