
# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally version of a variable can be created.

# Order of  scope
# 1] L = uses local scope 
# 2] E = uses encloseing scope
# 3] G = uses global scope
# 4] B = uses built-in scope

name = "Aman"              # global scope {available inside & outside function}

def display_name():
    name = "Patil"         # local scope {available only inside this function}
    print(name)
    
print(name)
display_name()