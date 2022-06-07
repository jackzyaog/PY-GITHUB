# -*- coding: utf-8 -*-

def triange1(n):
    LL1 = []
    for x in range(n):
        LX = []
        for i in range(x+1):
            if i == 0 :
                j = 1
                LX.append(j)
            elif ((i == x) and (i != 0)) :
                j = 1 
                LX.append(j)
            else :
                j = LL1[x-1][i-1]+LL1[x-1][i]
                LX.append(j)
        LL1.append(LX)
        yield(LL1[-1])

# print(triange1(6))
for t in triange1(6):
    print(t)

# print(triange1(10))
for t in triange1(10):
    print(t)

# print(triange1(15))
for t in triange1(15):
    print(t)  

# print(triange1(20))
for t in triange1(20):
    print(t)

print('new world')
