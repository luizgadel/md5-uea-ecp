from utils.funcoes_auxiliares import *
from utils.string_utils import *
from utils.int_utils import *

tam_nibble = 4
tam_palavra = 32
n_palavras_por_bloco = 16
tam_bloco = n_palavras_por_bloco*tam_palavra


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


def extensao_passo_2(msg_passo_1, b):
    b_64bit = converteIntParaBinario(b, 64)
    return msg_passo_1 + b_64bit


T = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
    0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391,
]

S = [
    [7, 12, 17, 22],
    [5, 9, 14, 20],
    [4, 11, 16, 23],
    [6, 10, 15, 21]
]

indices_de_X = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12,
    5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2,
    0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9,
]

mensagem = input("Digite a mensagem:")
tam_msg_original = len(mensagem)
msg_binaria = converteStrParaBinario(mensagem)

# Passo 1: Extens??o com bits de preenchimento
msg_passo_1 = extensao_passo_1(msg_binaria)

# Passo 2: Extens??o com o valor do tamanho
msg_passo_2 = extensao_passo_2(msg_passo_1, tam_msg_original)
tam_msg_p2 = len(msg_passo_2)

# Passo 3: Inicializar Buffer MD
MD_buffer = {
    "A": 0x67452301,
    "B": 0xefcdab89,
    "C": 0x98badcfe,
    "D": 0x10325476
}

# Passo 4: Processamento da mensagem em blocos de 16 palavras
n_blocos = tam_msg_p2 // tam_bloco
for i in range(n_blocos):
    bloco_i = msg_passo_2[i*tam_bloco:(i+1)*tam_bloco]
    X = []
    for j in range(n_palavras_por_bloco):
        inicio_p = tam_palavra*j
        iesima_palavra = msg_passo_2[inicio_p:inicio_p+tam_palavra]
        iesima_palavra_int = int(iesima_palavra, base=2)
        X.append(iesima_palavra_int)

    A = MD_buffer["A"]
    AA = A
    B = MD_buffer["B"]
    BB = B
    C = MD_buffer["C"]
    CC = C
    D = MD_buffer["D"]
    DD = D

    for k in range(64):
        k_mod_4 = k % 4
        k_div_16 = (k // 16)
        num_round = k_div_16 + 1
        if (k_mod_4 == 0):
            A = fun_round(A, B, C, D, X[indices_de_X[k]], S[k_div_16][k_mod_4], T[k], num_round)
        elif (k_mod_4 == 1):
            D = fun_round(D, A, B, C, X[indices_de_X[k]], S[k_div_16][k_mod_4], T[k], num_round)
        elif (k_mod_4 == 2):
            C = fun_round(C, D, A, B, X[indices_de_X[k]], S[k_div_16][k_mod_4], T[k], num_round)
        else:
            B = fun_round(B, C, D, A, X[indices_de_X[k]], S[k_div_16][k_mod_4], T[k], num_round)

    MD_buffer["A"] = A + AA
    AA = MD_buffer["A"]
    MD_buffer["B"] = B + BB
    BB = MD_buffer["B"]
    MD_buffer["C"] = C + CC
    CC = MD_buffer["C"]
    MD_buffer["D"] = D + DD
    DD = MD_buffer["D"]

bin_A = converteIntParaBinario(AA, 32)
bin_B = converteIntParaBinario(BB, 32)
bin_C = converteIntParaBinario(CC, 32)
bin_D = converteIntParaBinario(DD, 32)

md = binParaHex(bin_A) + binParaHex(bin_B) + binParaHex(bin_C)  + binParaHex(bin_D)
print(f"Hash: {md[0:6]} -> {md}")