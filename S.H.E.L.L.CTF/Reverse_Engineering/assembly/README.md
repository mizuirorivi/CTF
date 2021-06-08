# asm_code

## description 
関数のアセンブリファイルが渡されて、それを地道に読み解く問題
fun1(0x74,0x6f) + fun1(0x62,0x69) = ?
をflagとしてSHELL{0x????}形式で渡せばいい

## Solution 
こちらがアセンブリファイル
```
fun1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    <fun1+28>
	<+20>:	add    DWORD PTR [ebp-0x4],0x7
	<+24>:	add    DWORD PTR [ebp-0x8],0x70
	<+28>:	cmp    DWORD PTR [ebp-0x8],0x227
	<+35>:	jle    <fun1+20>
	<+37>:	mov    eax,DWORD PTR [ebp-0x4]
	<+40>:	leave  
	<+41>:	ret 
```

これを自分で擬似コードにしてみた。
```
func1(arg1,arg2){
    int var_4h;
    int var_8h;
    var_4h = arg2;
    var_8h = arg1;
    while(True){
        if(var_8h <= 0x227){
            var_4h += 0x7;
            var_8h += 0x70;
        }else{
            return var_4h;
        }
    }
}
```

### Solveコード
```
def fun1(arg1,arg2):

    var_4h = arg2
    var_8h = arg1

    while True:
        if var_8h <= 0x227:
                var_4h += 0x7
                var_8h += 0x70
        else:
            return var_4h
print("SHELLCTF{" + hex(fun1(0x74,0x6f) + fun1(0x62,0x69)) + "}")
```
