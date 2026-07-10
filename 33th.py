
import os

path = "C:\\Users\\DELL\\OneDrive\\Desktop\\PROGRAM\\.vscode\\New folder"

if os.path.exists(path):
    print("That location exists !")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exists !")