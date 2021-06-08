def fun1(arg1,arg2):

    var_4h = arg2
    var_8h = arg1

    while True:
        if var_8h <= 0x227:
                var_4h += 0x7
                var_8h += 0x70
        else:
            return var_4h
print("SHELLCTF{" + hex(fun1(0x74,0x6f) + fun1(0x62,0x69)) + "}")

        