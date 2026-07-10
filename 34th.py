
try:
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\PROGRAM\\.vscode\\New folder\\text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")