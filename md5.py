def imprimeBinario(bin):
    if (len(bin) > 20): 
        msg = f"Tam: {len(bin)} - Bin: {bin[:10]}...{bin[-10:]}" 
    else: 
        msg = f"Tam: {len(bin)} - Bin: {bin}"
    
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
        tam_final = ((tam_atual_msg - congruent) // modulo + 1) * modulo + congruent
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