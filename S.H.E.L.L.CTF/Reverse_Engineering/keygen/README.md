# keygen

## description 
入力した文字を文字列で比較している
## Solution
比較している文字を代入してあげるとフラグが得られる

### solveコード
```
def checkends(password):
    password[:6] = "SHELL{"
    password[28] = "}"
def checkmiddle1(password):
    password[27] = "1"  
    password[17] = "4" 
    password[8] = "n" 
    password[23] = "y" 
    password[10] = "0"
    password[11] = "n"
    password[12] = "z"  
    password[13] = "a"  
    password[21] = "g" 
    password[15] = "u"
    password[16] = "r"
    password[7] = "3"
def checkmiddle2(password):
    password[18] = "_"  
    password[25] = "5"  
    password[20] = "4"  
    password[14] = "k"  
    password[22] = "3"  
    password[9] = "b"   
    password[24] =  "0"

    password[19] = "k" 
    password[26] = "h" 
    password[6] = "s"
# driver?!?jedi=0,  code?!? (*_*prompt: Any=...*_*) ?!?jedi?!?
s = "SHELL{aaaaaaaaaaaaaaaaaaaaaa}"
a= list(s)
checkends(a) 
checkmiddle1(a)
checkmiddle2(a) 
print("".join(a)
```