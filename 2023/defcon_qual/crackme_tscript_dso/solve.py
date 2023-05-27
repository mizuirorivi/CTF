file_path = "./crackme.tscript.dso"  # Replace with the actual path to your file
# L*C.C1
del_content1=b"\x4c\x2a\x43\x2e\x43\x31"
#L*C+4
del_content2=b"\x4c\x2a\x43\x2b\x34"
#L*C.CD
del_content3=b"\x4c\x2a\x43\x2e\x43\x44"

del_contents = [del_content1 , del_content2, del_content3]
# Open the file in read mode
file = open(file_path, "rb")
file_contents = file.read()
ba_file_contents = [] 
for i in range(0, len(file_contents)):
    content = file_contents[i:i+16]
    ba_content = bytearray(content)
    for d in del_contents:
        if d.hex() in content.hex():
            bc = bytearray(content)
            print(bc)
            c = bc.replace(bytearray(d),bytearray())
            print(c)
            ba_content = c
    ba_file_contents.append(ba_content)
with open('new_binrary.dso','wb') as f:
    for i in ba_file_contents:
        f.write(i)

    
