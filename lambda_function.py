# def xya(x,y):
#     return x+y

#lambda -> one line function

#syntax
#f_name = lambda para:exp
add = lambda x,y:x+y
print(add(1,2))


l1 = [1,2,3,4,5,6] #even ->2,4,6
l2 = list(filter(lambda x:x%2==0,l1)) #x%2==0 True -> list 
print(l2)