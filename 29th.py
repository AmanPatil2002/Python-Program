
# str.format() = optional method that gives users
#                more cntrol when displaying output

name = "Aman"

print("Hello, my name is {}".format(name))
# Padding
print("Hello, my name is {:10}.Nice to meet you".format(name))      #Default 
print("Hello, my name is {:<10}.Nice to meet you".format(name))     #Left
print("Hello, my name is {:>10}.Nice to meet you".format(name))     #Right
print("Hello, my name is {:^10}.Nice to meet you".format(name))     #Center