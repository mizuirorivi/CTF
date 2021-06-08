BruteforceRSA
100
Flag Format : shellctf{}

## description 
```
{"e": 65537, "n": 105340920728399121621249827556031721254229602066119262228636988097856120194803, "enc_msg": 36189757403806675821644824080265645760864433613971142663156046962681317223254}
```

```
from Crypto.Util.number import bytes_to_long, inverse, getPrime, long_to_bytes
from secret import message
import json

p = getPrime(128)
q = getPrime(128)

n = p * q
e = 65537

enc = pow(bytes_to_long(message.encode()), e, n)
print("Encrypted Flag is {}".format(enc))

open('./values.json', 'w').write(json.dumps({"e": e, "n": n, "enc_msg": enc}))
```
## Solution 
ご存知の通り
e,n,cがあるので例のサイトを使ってpとqを求めた
p = 320163545884759912335372936276795190799
q = 32902222030710414212194772416290447279
よってdが求められるので平文を計算して終了


shellctf{k3y_s1ze_m@tter$}
### solveコード
```
from Crypto.Util.number import bytes_to_long, inverse, getPrime, long_to_bytes,inverse
import json
import math

p = 320163545884759912335372936276795190799
q = 329022220307104142121947724162904472797

c = 36189757403806675821644824080265645760864433613971142663156046962681317223254
l = math.lcm(p-1,q-1)
n = 105340920728399121621249827556031721254229602066119262228636988097856120194803
e = 65537
d = inverse(e,l)
m = hex(pow(c,d,n))[2:]

dump = (bytes.fromhex(m)).decode("utf-8")
print(dump)
```


