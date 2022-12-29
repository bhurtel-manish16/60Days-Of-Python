a = [1,2,3]
b = (1,2,3)
c = b * 3
print(c)

a[0]  =10
print(a[0])
#b[0] = 10
# print(b[0])
# del a
# print(a)

for i in b:
    print(i)

print(b.count(2))
print(b.index(3))