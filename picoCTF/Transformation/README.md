# Transformation 

###### tags: `ctf` `bin`

###### author: `MADSTACKS`

points: `20`

-------

## Description

>I wonder what this really is... [enc](https://mercury.picoctf.net/static/2b4cea9b07db22bf4f933fddd1b8caa9/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

