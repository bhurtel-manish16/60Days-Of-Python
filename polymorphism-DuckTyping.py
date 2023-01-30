# Poly morphism  
#Duck typing --/ House | Duck

# a = 10
# print(type(a))
# a = "STR"
# print(type(a))

class Duck:
    def walk(self):
        print("Tuk tuk")

class Dog:
    def walk(self):
        print("BHU BHU")

class Cat:
    def walk(self):
        print("MEW MEW")

def beings(obj):
    obj.walk()

d = Duck()
d1 = Dog()
c = Cat()
beings(d)
beings(d1)
beings(c)

