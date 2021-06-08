from pwn import *
print('ばーかばーか')
io = remote('localhost',4088)
t = io.recvline()
print(t)
io.recvuntil('welcome(): ')
var1 = int(io.recvline(),16)
log.info("addr of welcome {}",p64(var1))
io.interactive()
