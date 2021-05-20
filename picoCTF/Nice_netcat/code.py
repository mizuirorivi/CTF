import subprocess

ans = ""
with open('./test.txt') as f:
    s = f.read()
    s = s.replace('\n','')
    t = s.split(' ')
    t.pop()
    for i in t:
        ans += chr(int(i))
        
print(ans)