# Python model for four bits multiplier

def four_bits_multiplier(a, b):

    mult_int = a * b

    mult_bin = bin(mult_int)[2:]
    mult_bin = mult_bin.zfill(8)

    mult = int(mult_bin,2)

    return mult