# toBinStringN

def toBinStringN(a, N):
    """
    convert decimal to N-bit Two's Complement form
    """
    if a >= 0:
        str_a = bin(a)[2:]
        len_a = len(str_a)
        return str_a.zfill(N)
    else:
        maskN = int('0b' + '1' * N, 2)
        str_a = bin(a & maskN)[2:]
        return str_a.zfill(N)