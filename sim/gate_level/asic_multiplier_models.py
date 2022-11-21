# Python model for 4bit_dataiplier

"""
     -- 1 --
    |       |
    6       2
    |       |
     -- 7 --
    |       |
    5       3
    |       |
     -- 4 --
"""

def seven_segs_to_number(segments):

    if segments == 0b0111111:
        digit = 0
    elif segments == 0b0000110:
        digit = 1
    elif segments == 0b1011011:
        digit = 2
    elif segments == 0b1001111:
        digit = 3
    elif segments == 0b1100110:
        digit = 4
    elif segments == 0b1101101:
        digit = 5
    elif segments == 0b1111100:
        digit = 6
    elif segments == 0b0000111:
        digit = 7
    elif segments == 0b1111111:
        digit = 8
    elif segments == 0b1100111:
        digit = 9
    elif segments == 0b1110111:
        digit = 10
    elif segments == 0b1111100:
        digit = 11
    elif segments == 0b0111001:
        digit = 12
    elif segments == 0b1011110:
        digit = 13
    elif segments == 0b1111001:
        digit = 14
    elif segments == 0b1110001:
        digit = 15
    else:
        digit = 0
        
    return digit

def digits_to_number(msb, lsb):

    msb_bin = bin(msb)[2:]
    msb_bin = msb_bin.zfill(4)

    lsb_bin = bin(lsb)[2:]
    lsb_bin = lsb_bin.zfill(4)

    res_bin = msb_bin + lsb_bin

    number = int(res_bin,2)

    return number