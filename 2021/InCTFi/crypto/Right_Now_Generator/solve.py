#!/usr/bin/env python3

import random
import hashlib
import os
import gmpy2
import pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


FLAG = open('enc.pickle', 'rb').read()


class Solve():
    pad = 0xDEADC0DE
    sze = 64
    mod = int(gmpy2.next_prime(2**sze))

    def __init__(self, seed_val, seed=None):
        if seed == None:
            assert seed_val.bit_length() == 64*2, "Seed is not 128 bits!"
            self.seed = self.gen_seed(seed_val)
            self.wrap()
        else:
            self.seed = seed
            self.ctr = 0


def main():
    random.getrandbits(128)
