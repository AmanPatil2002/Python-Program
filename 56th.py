# Higher Order Functions = A function that either:
#                           1. accepts a function as a argument
#                                        or
#                           2. returns a function
#                              (In python, functions are also treated as objects)

# Example = 2. returns a function

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))