# map() = applies a function to each item in an iterable (list, tuple, etc.)

# map(function,iteration)

store =(["shirt",562.00],
        ["pant",700.00],
        ["jacket",962.00],
        ["socks",50.00])

to_euros = lambda data: (data[0],data[1]*0.82)     # to convert into euros
to_dollars = lambda data: (data[0],data[1]/0.82)   # to convert into dollar

#store_euros = list(map(to_euros,store))
store_dollars = list(map(to_dollars,store))

for i in store_dollars:
    print(i)