
# str.format() = optional method that gives users
#                more cntrol when displaying output

animal = "Lion"
item = "meat"

#print("The "+ animal +" is eating "+ item)

#print("The {} is eating {}".format("Lion","meat"))
#___________or_____________.format(animal,item)

#print("The {0} is eating {1}".format(animal,item))  #positional argument

#print("The {animal} is eating {item}".format(animal="Lion",item="meat"))   #keyword argument

text = "The {} is eating {}"
print(text.format(animal,item))
