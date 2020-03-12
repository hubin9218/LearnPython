for x in range(100,1000):
    ge = x % 10
    shi = x // 10 % 10
    bai = x // 100
#    if(ge ** 3 + shi ** 3 + bai ** 3 == x):
#        print()

y = '=='+str(x)+'=='
#print(y)

a = 1
b = 1
c = a+b
d = b+c
e = d+c
print(a,b,c,d,e)


a ,b= 0, 1
for _ in range(5):
    a,b= b, a + b
    print(a)