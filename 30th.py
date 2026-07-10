
# str.format() = optional method that gives users
#                more cntrol when displaying output

number = 3.14159
numbers = 1000

print("The number pi is {:.2f}".format(number))     # To addjust points
print("The number pi is {:,}".format(numbers))      # To add coma(,)
print("The number pi is {:b}".format(numbers))      # To convert into Binary
print("The number pi is {:o}".format(numbers))      # To convert into Octal
print("The number pi is {:X}".format(numbers))      # To convert into Hexa-decimal
print("The number pi is {:E}".format(numbers))      # To convert into Scientific notation