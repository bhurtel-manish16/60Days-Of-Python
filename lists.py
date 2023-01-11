import random
# int
# str
# float
# bool
# list
# dict
# set
# tuple
# b = [5,6]

#ADD VALUE IN A LIST
# for i in range(5):
#     b.append(i)
# # a[index] = value

# print(b)
# b.pop(2)
# print(b)
# b.pop()
# print(b)

#pos 1-index 0, pos 2-index 1
# a = [10,20,30,40,50] #index list - > 0
# a[0] = 50
# a.append(60) #to add value
# print(a)
# a.pop() #to delete last value
# print(a)
# a.sort() #to sort values in the list
# print(a)

# b = ["manish","joe","xyz"]
# print(b)
# c = [10,"manish",True]
# print(c)


#ADD RANDOM VALUES TO A LIST

val = []

for i in range(10):
    val.append(random.randint(10,1000))
print(val)


#To take input from user
#1
# print('Enter your name')
# name = input()
#2
# name = input("Enter your name: ")
# print(name)

#To take five values form user and print the list
# fruits=[]
# print("Enter fruit's name ")
# for i in range(5):
#     fruit_name=input()
#     fruits.append(fruit_name)

# print (fruits)

# fruit=[]
# for i in range(5):
#     f_name=input("enter fruit name: ")
#     fruit.append(f_name)
# print(fruit)

#------------------DAY 2-------------------

# list1 = [1,2,2,2,3,4,5,6]
# list1.reverse()
# print(list1)
# b = [7,8,9]
# list1.extend(b)
# b.clear()
# print("count")
# print(list1.count(2))


# print(list1)
# for i in list1:
#     if i % 2 == 0:
#         print("even")

#slicing

var = "Hello This is test"
print(var.split(" "))
print(var)


input1 = int(input("Enter number of element: ")) #10 llist 10 

list2 = []
for i in range(0,input1):
    list2.append(random.randint(0,1000))
print(list2)
print(list2[0:int(len(list2)/2)])
print(list2[int(len(list2)/2):])

x = "manish"
print(x.replace("i",","))