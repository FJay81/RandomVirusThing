from VirusTool import VT
import glob
text = str(input("What would you like to write"))
for files in glob.glob("*.txt"):
    file = VT(files)
    file.change(text)
