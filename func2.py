# def fun1(**name):
#     return name

# name1 = input("Enter your name: ")
# print(fun1(name=name1,age=12,id=101)["name"])
#id name age

#proj: calc
#add, sub, mul, div

def get_input():
    n1 = int(input("Enter first num: "))
    n2 = int(input("ENter sec num: "))
    return n1,n2

def add(num1,num2):
    return num1+num2


def sub(num1,num2):
    return num1-num2


def mult(num1,num2):
    return num1*num2


def div(num1,num2):
    return num1/num2


def user_ch():
    print("Enter 1 to add")
    print("Enter 2 to sub")
    print("Enter 3 to mult")
    print("Enter 4 to div")
    user_fd = int(input())
    return user_fd



def cal(user_fd):
    if user_fd == 1:
        results = get_input() #tuple (10,20)
        num1 = results[0] #10
        num2 = results[1] #20
        res = add(num1,num2)
        print(res)
    elif user_fd == 2:
        results = get_input() #tuple (10,20)
        num1 = results[0] #10
        num2 = results[1] #20
        res = sub(num1,num2)
        print(res)
    elif user_fd == 3:
        results = get_input() #tuple (10,20)
        num1 = results[0] #10
        num2 = results[1] #20
        res = mult(num1,num2)
        print(res)
    elif user_fd == 4:
        results = get_input() #tuple (10,20)
        num1 = results[0] #10
        num2 = results[1] #20
        res = int(div(num1,num2))
        print(res)
    else:
        print("INvalid input")
        main()


def main():
    cal(user_ch())


main()
# print(add(res,res2))
#user choice