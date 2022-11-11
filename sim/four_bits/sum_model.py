# Python model for four bits adder

def four_bits_adder(a, b, cin):

    sum_int = a + b + cin

    sum_bin = bin(sum_int)[2:]
    sum_bin = sum_bin.zfill(5)

    sum = sum_bin[1:5]
    sum = int(sum,2)
    carry = int(sum_bin[0])

    return carry, sum