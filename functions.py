# def function_name(para,....., *para): #user defined func
#     ....statemen

# print("hello") #built in func
#len()
# def show_msg():
#     print("Hello welcome back!")


# show_msg()


#types of func
#1- Task display
#2 - task return

print("len: "+str(len("my")))
#user defined func
def add_num(a,b):
    add = a+b
    print(add)

def add_num1(a,b):
    add = a+b
    return add

#Built in func
# print("hi")
# print(len("my"))

# add_num(1,2)
# print(add_num1(1,2))

#Reeturning value
# def show_name(name):
#     return (f"Hi {name}")

# def show_name(name):
#     print(f"Hi {name}")
#     #reutrn none default

# print(show_name("Manish"))

# def calc(*nums):
#     sum = 0
#     for i in nums:
#         sum += i #sum = sum+i #sum = 10+20 = 30
#     print(sum)
#     # return "test"

# calc(10,20)
# print(calc(10,20))

# calc(10,20,30,40,50,60,70)
# print(calc(10,20))

#QUS 10 > ? num 
#1 5 10 12 45

num1 = 10
num1 = 30
#overwrite and override
def calc(a,b=20):
    return a+b

print(calc(10,30))

# def check_greater(*nums):
#     count = 0
#     for i in nums: #for i in range(10,20)
#         if i >= 10:
#             count += 1
#     return count
#keyword

# print(check_greater(1,4,10,30,40,22))

#scope in func
#scope 2-> local and global
count = 10 #global
def check_greater(*nums):
    count = 0 
    for i in nums: #for i in range(10,20)
        if i >= 10:
            count += 1
    return count

def chrs(count, *a):
    print(count)

chrs(count)
print(count)
print(check_greater(2,3,4,10))