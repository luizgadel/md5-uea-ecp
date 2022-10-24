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


def string_reversa(str):
    return str[::-1]
