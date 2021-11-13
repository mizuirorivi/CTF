import string
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
key = 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890'

text = "HITSS{5X65Z1ZXZ10F_E1LI3J}"
def decrypter(text,key):
    decrypted_msg = ''
    for i in text:
        index = key.index(i)
        decrypted_msg += alpha[index]
    
    return decrypted_msg

print(decrypter(text,key))