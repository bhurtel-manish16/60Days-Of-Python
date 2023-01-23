class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        # self.onr = self.owner() Method 1
    
    def show_info(self):
        print(self.brand, self.color)

    class owner:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        
        def show_info(self):
            print(self.name, self.age)

c1 = car("BMW","RED")
c1.show_info()
# c1.onr.show_info() obj 1

onr = car.owner("John",32)
onr.show_info()