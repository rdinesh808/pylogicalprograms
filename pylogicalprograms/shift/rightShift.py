
# 65536 32768 16384 8192 4096 2048 1024 512 256 128 64 32 16 8 4 2 1

def right_shift(number, rshift):
    shift = 2 ** rshift
    return number // shift
