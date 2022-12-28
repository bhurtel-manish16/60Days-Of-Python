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

fruit=[]
for i in range(5):
    f_name=input("enter fruit name: ")
    fruit.append(f_name)
print(fruit)