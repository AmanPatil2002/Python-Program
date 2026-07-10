
# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Aman",20,"Male")

print(student.count("Aman"))
print(student.index("Male"))

for x in student:
    print(x)

if "Aman" in student:
    print("Aman is here")