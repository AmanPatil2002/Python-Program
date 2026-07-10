# filter() = creates a collection of elements from an iterable for which a function returns true

# filter(function, iteration)

friends = [("Aman",21),
            ("Nida",20),
            ("Musa",19),
            ("Anzar",14),
            ("Araish",13),
            ("Nuhaid",8)]

age = lambda data:data[1] >=18

Driving_licence = list(filter(age, friends))

for i in Driving_licence:
    print(i)