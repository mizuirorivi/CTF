# MatchTheRegex

###### tags: `picoctf` `web` `regex`

```python
import requests
url = 'http://saturn.picoctf.net:49937/'

r = requests.get(url+'flag?'+'input='+'picoCTF.*')
print(r.text)
                 
```

```
└─$ python solve.py 
{"flag":"picoCTF{succ3ssfully_matchtheregex_8ad436ed}"}
```

