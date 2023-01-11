#Recurion


def count(n):
    if n > 0:
        print(n)
        count(n-1)
    return 0

count(10)


#facto

#5! = 5*4*3*2*1

def facto(n):
    if n <= 1:
        return 1
    return n*facto(n-1)

print(facto(5))

#facto(5) n = 5
#5*facto(4) n =4
#5 * 4 * facto(3) n = 3
#5 * 4* 3* facto(2) n = 2
#5 * 4* 3 * 2 * fact(1) n = 1
#5*4*3*2*1 = 120
#0 + 1 1+1 2+1 3
#0 1 1 2 3 5 8................nth