# CLASS
# a = 10
# # def fun(a): MEHTOD
# #     return a**2

#OBJ o1
#o2, o3 , o4

#syntax
# class classname:
#     #attr
#     #method

#var = classname

class dog:
    def __init__(self):
        print("i")

    name = "abcd"
    def show_name(name):
        print("name of the dog is: ",name)

 
d1 = dog
d1.show_name(d1.name)
d2 = dog
d2.show_name(d2.name)
