
# slicing = create a substring by extracting elementsfrom another string
#           indexing[]          or      slice()
#           [start:stop:step]           (start,stop,step)

################################indexing[]################################

name = "Aman Patil"

#   start
first_name = name[0:4]
#  or      = name[:4]

#   stop
last_name = name[5:10]
#  or     = name[5:]

#   step
funky_name = name[0:10:3]
#  or      = name[::3]

reversed_name = name[::-1]

print("First name :"+first_name)
print("last name :"+last_name)
print("Funky name :"+funky_name)
print("Reversed name :"+reversed_name)

##################################slice()##################################

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
