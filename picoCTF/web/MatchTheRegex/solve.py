import requests
url = 'http://saturn.picoctf.net:49937/'

r = requests.get(url+'flag?'+'input='+'picoCTF.*')
print(r.text)
