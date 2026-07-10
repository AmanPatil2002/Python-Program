
import os
#import shutil

path = "text.txt"

try:
    os.remove(path)           # To delete a file
    #os.rmdir(path)           # To delete an empty directory
    #shutil.rmtree(path)      # To delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")