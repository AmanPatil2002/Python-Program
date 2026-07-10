
# keyword arguments = arguments preceded by an identifieer when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)
 
hello(middle="Ajit",last="Patil",first="Aman")