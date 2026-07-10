# list comprehension = A way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
                    
students = [100,90,80,70,60,50,40,30,0]

#passed_students = list(filter(lambda x: x >= 60, students))              #list = [expression for item in itrable]

#passed_students = [i for i in students if i >= 60]                       #list = [expression for item in itrable if conditional]

passed_students = [i if i >= 60 else "Failed" for i in students]          #list = [expression (if/else) for item in itrable]

print(passed_students)