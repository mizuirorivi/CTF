from pwn import *

r = remote('mercury.picoctf.net','53437')

r.recvuntil('2) View my portfolio')
