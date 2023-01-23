class car:

    w = 4
    def __init__(self):
        self.brand = "BMW"
        self.color = "RED"

    
c1 = car()
c2 = car()
print(car.w)
car.w = 5
print(car.w)
print(c1.brand)
c1.brand = "ABC"
print(c1.brand)
print(c2.brand)
print(car.w)