def int_to_signed_string(i,bits):
    return hex(i & ((1<<bits) - 1 ))

def signed_string_to_int(s,bits):
    ss = int(s,16)
    return -(ss & (1<<(bits-1))) | ss

bits = 64
int2ss = lambda i: int_to_signed_string(i,bits)
ss2int = lambda s: signed_string_to_int(s,bits)

test = [-128, -127, -2, -1, 0, 1, 2, 126, 127]
test_str_hex = []

print(int2ss(-559038242))
    