# sort() method = used with lists
# sort() function = used with iterables

students =[("Aman","A",89),
           ("Rahul","B",77),
           ("Samarth","F",39),
           ("Tusar","C",63),
           ("Anil","D",52),]

# sorted with grade
#grade = lambda grades:grades[1]
#students.sort(key=grade)

#/////////////////////////////////////////////////////////////////////////////////////////

# sorted with marks
mark = lambda marks:marks[2]
students.sort(key=mark)

for i in students:
    print(i)