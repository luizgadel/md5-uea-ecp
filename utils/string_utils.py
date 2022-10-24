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


def string_reversa(str: str):
    return str[::-1]


def binParaHex(b: str):
    b_revertido = string_reversa(b)
    tam_bin = len(b)
    tam_byte = 8
    n_bytes = tam_bin//tam_byte
    msg = ""
    for i in range(n_bytes):
        byte_i = b_revertido[i*tam_byte:(i+1)*tam_byte]
        byte_int_value = int(byte_i, base=2)
        h = hex(byte_int_value)
        msg += h[2:]
    return msg