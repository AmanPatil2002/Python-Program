
# logical operators (and,or,not) = used to check if two or more conditional statement is true

temp = int(input("What is the temperature outside ? : "))

#  and operator
#if temp >= 0 and temp <= 30:
    #print("The temperature is good today")
    #print("Go outside")

#  or operator
#elif temp < 0 or temp > 30:
    #print("The temperature is bad today")
    #print("Stay inside")

#  not operator
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today")
    print("Stay inside")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside")