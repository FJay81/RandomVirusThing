from VirusTool import Naming
import glob
text = str(input("What would you like to write"))
for files in glob.glob("*.txt"):
    file = Naming(files)
    file.change(text)