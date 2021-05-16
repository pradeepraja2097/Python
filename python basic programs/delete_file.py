import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("the file does not exist")
