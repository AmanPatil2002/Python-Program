
# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a fuction can accept a varing amount of keyword arguments

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(first="Aman",middle="Ajit",last="Patil")
