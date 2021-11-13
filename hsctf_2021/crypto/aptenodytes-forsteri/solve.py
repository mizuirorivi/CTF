flag = open('output.txt','r').read() #open the flag

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decoded = ""
for character in flag:
    decoded+=letters[(letters.find(character)-18)%26] #encode each character
print(decoded)
