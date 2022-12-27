# Operators
# a = 10
# a += 1 #a = a +1
# print(a)
# a -= 2 #a = a-2
# print(a)
# a /= 2
# print(a)
# print(a**2)

# & | 
a = 10 # 8 4 2 1 -> 1010
b = 12 # 8 4 2 1 -> 1100
                    #1110 8+4+2 -> 14
print(a|b)


# Decision
# == compare
# != Not equals to
# <= less than or equal to
# >= gr ot eql to
# AND OR NOT gate
# AND 1 1 -> 1. 1 0 -> 0
# OR 1 1 -> 1. 0 1 -> 1


# print(a==b)
# print(a!=b) # 1 0 OR -> 1
# print(a<=b) # 1 0 OR -> 1
# print(a>=b) # 0 0 OR -> 0

a = 100
b = 50
c = 300

if a > b and a > c: 
    print(a)
elif b > c:
    print(b)
else:
    print(c)

a = 100
b = 20
a,b = b,a
print(a,b)
a = a + b # 30
b = a - b # 30 - 20 -> 10
a = a - b # 30 - 10 -> 20
print(a,b)
# a = 20 b = 10