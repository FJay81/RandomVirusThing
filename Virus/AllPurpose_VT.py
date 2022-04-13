from VirusTool import VT

while True:
    select = int(input("Press '1' for encryption(Only works on existing files!):\nPress '2' for custom modification(Will overwrite any existing text!):\n"))
    fname = str(input("File Name.extension\n"))
    ok = VT(fname)
    if select == 1:
        rm = int(input("random number"))
        ok.encrypt(rm)
    elif select == 2:
        code = str(input("What do you want to write"))
        ok.change(code)