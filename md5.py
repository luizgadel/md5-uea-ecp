def converteParaBinario(msg):
    bin_msg = ""
    for caractere in msg:
        bin_msg += bin(ord(caractere))[2:]
    return bin_msg

def extensao(msg_binaria):
    congruent = 448
    modulo = 512

    msg_estendida = (msg_binaria + '1')
    
    tam_atual_msg = len(msg_estendida)
    if (tam_atual_msg >= congruent):
        tam_final = ((tam_atual_msg - congruent) // modulo + 1) * modulo + congruent
    else: 
        tam_final = congruent

    print("[ Tamanho pós-conversão:", tam_final, ']')
    msg_estendida = msg_estendida.ljust(tam_final, '0')
    return msg_estendida

mensagem = input("Digite a mensagem:")
msg_binaria = converteParaBinario(mensagem)
print("Tam:", len(msg_binaria))
print("Bin:", msg_binaria)

print("\n((Passo 1: Extensão))")
mensagem_estendida = extensao(msg_binaria)
print("Tam:", len(mensagem_estendida))
print("Bin:", mensagem_estendida)