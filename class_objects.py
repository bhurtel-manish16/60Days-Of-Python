class cars: #brand #color
    def __init__(sa, brand, color):
        sa.brand = brand
        sa.color = color
    

    def show(self):
        print("Brand is ",self.brand)
        print("color is ",self.color)
        

c1 = cars("BMW","RED")
c1.brand = "b"
c1.color="green"
c2 = cars("a","yellow")
c2.color = "RED"
c1.show() 
c2.show()