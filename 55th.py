# Higher Order Functions = A function that either:
#                           1. accepts a function as a argument
#                                        or
#                           2. returns a function
#                              (In python, functions are also treated as objects)

# Example = 1. accepts a function as a argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)
    
hello(loud)
hello(quiet)