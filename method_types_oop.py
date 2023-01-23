class school:
    name = "ABC"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    

    @classmethod
    def get_name(cls):
        return cls.name

    @staticmethod
    def get_num():
        for i in range(0,10):
            print(i)

    #Getter and setter
    # def get_m1(self):
    #     return self.m1
    
    # def set_m1(self,val):
    #     self.m1 = val

    
s1 = school(10,20,30)
# s1.set_m1(100)
print(s1.get_avg())
# print(s1.get_m1())
print(school.get_name())
school.get_num()