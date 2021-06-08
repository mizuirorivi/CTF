# ALGORIC-SHIFT
## description
```
ciphered text : HESL{LRAT5PN51010T_CNPH1R}3

Try decrypting:
```
暗号化のスクリプトがこちら
```
text = 'flag{...}'
key = [3, 1, 2]

li0 = []
li1 = []
li2 = []
for i in range(0, len(text)):
    if i % 3 == 0:
        li0.append(text[i])
    elif (i - 1) % 3 == 0:
        li1.append(text[i])
    elif (i - 2) % 3 == 0:
        li2.append(text[i])
li = []
for i in range(len(li1)):
    li.append(li1[i])
    li.append(li2[i])
    li.append(li0[i])

# print(li)
print("The ciphered text is :")
ciphered_txt = (''.join(li))
print(ciphered_txt)
```
## Solution 
頭が働かなかったのでとりあえず何回か暗号化されたフラグを更に暗号化させてた。
そしたらフラグが見つかったのでオールok
```
mizuiro@mizuiro-arch ~/P/c/S/C/Algoric-Shift (main)> python3 script.py
HESL{LRAT5PN51010T_CNPH1R}3
The ciphered text is :
ESH{LLATRPN51050T1CN_H1P}3R
mizuiro@mizuiro-arch ~/P/c/S/C/Algoric-Shift (main)> python3 script.py
ESH{LLATRPN51050T1CN_H1P}3R
The ciphered text is :
SHELL{TRAN5P051T10N_C1PH3R}
```