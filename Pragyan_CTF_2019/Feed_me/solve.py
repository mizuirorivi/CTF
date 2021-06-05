from pwn import *
import sys
from z3 import *

io = remote('localhost',4077)
io.recvline()
var1 = int(io.recvuntil(' ;').rstrip(b';'))
var2 = int(io.recvuntil(' ;').rstrip(b';'))
var3 = int(io.recvuntil(' ;').rstrip(b';')) 

log.info("{} {} {}".format(var1,var2,var3))
ivar4,ivar5,ivar6 = Ints('ivar4 ivar5 ivar6')
x = [var1,var2,var3]
solver = Solver()
solver.add(ivar5+ivar4 == x[0],ivar6+ivar5 == x[1],ivar4+ivar6==x[2])
solver.check()
m = solver.model()
log.info('{} {} {}'.format(m[ivar4],m[ivar5],m[ivar6]))

payload = ""
payload += str(m[ivar4])+(10-len(str(m[ivar4])))*'-'
payload += str(m[ivar5])+(10-len(str(m[ivar5])))*'-' 
payload += str(m[ivar6])+(10-len(str(m[ivar6])))*'-' 

log.info('payload = {}'.format(payload))
io.sendline(payload)
io.interactive()


