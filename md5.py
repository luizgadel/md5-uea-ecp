from utils.funcoes_auxiliares import *
from utils.string_utils import *
from utils.int_utils import *

tam_nibble = 4
tam_palavra = 16


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


def inicializa_md_buffer():
    MD_buffer_hex = {
        "A": "01234567",
        "B": "89abcdef",
        "C": "fedcba98",
        "D": "76543210"
    }
    MD_buffer = {}
    for w in MD_buffer_hex:
        nibble_bin = ""
        for nibble_hex in MD_buffer_hex[w]:
            nibble_bin += string_reversa(bin(int(nibble_hex, base=16))
                                         [2:].zfill(tam_nibble))
        MD_buffer[w] = nibble_bin

    return MD_buffer


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
    parcial_a_deslocar = a + resultado_f_aux + x + t
    a = b + (parcial_a_deslocar << s)
    return a


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
    7, 12, 17, 22,
    5, 9, 14, 20,
    4, 11, 16, 23,
    6, 10, 15, 21
]

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
tam_msg_p2 = len(msg_passo_2)

print("\nPasso 3: Inicializar Buffer MD")
MD_buffer = inicializa_md_buffer()
print(MD_buffer)

print("\nPasso 4: Processamento da mensagem em blocos de 16 palavras")
qtd_words = tam_msg_p2/tam_palavra
X = []
for i in range(qtd_words):
    inicio_p = tam_palavra*i
    iesima_palavra = msg_passo_2[inicio_p:inicio_p+tam_palavra]
    iesima_palavra_int = int(iesima_palavra, base=2)
    X.append(iesima_palavra_int)

    AA = MD_buffer["A"]
    BB = MD_buffer["B"]
    CC = MD_buffer["C"]
    DD = MD_buffer["D"]
    # round 1
