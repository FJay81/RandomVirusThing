class VT:
    def __init__(self,name):
        self.name = name
        pass 
    def __str__(self):
        return f"{self.name}"
    def change(self,Text):
        File = f"{self.name}"
        f = open(File, 'w')
        f.write(Text)
        f.close()  
    def encrypt(self,g):
        File = f"{self.name}"
        F = open(File, 'r')
        contents = F.read()
        F.close()
        arr = bytearray(contents, 'utf8')
        bytelist = []
        x = bytes()
        hashed = 0
        for byte in arr:
            x = (byte)
            h = (x*2)
            hashed = (h + x)
            bytelist.append(hashed)
        f = ''.join(str(e) for e in bytelist)
        k = f.encode('utf8')
        string = k.decode('utf8')
        code = int(string)   
        code = code*code
        code = code * g 
        Text = str(code)
        F = open(File, 'w')
        F.write(Text)
        F.close()
