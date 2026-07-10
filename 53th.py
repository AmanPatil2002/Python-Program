# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# Example 1____________________________________________________________

# happy = True
# print(happy)

#print(happy := True)       # walrus operator :=

# Example 2____________________________________________________________

#foods = list()
#while True:
#    food = input("What food do you like : ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("What food do you like : ") != "quit":
    foods.append(food)