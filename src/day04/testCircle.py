from math import sqrt
'''
a = int(input("a="))
result = True
for x in range(2,a):
    print(a,'%',x,'=',a%x)
    if a % x == 0:
        result = False
        break

if result:
    print('prime')
else :
    print('not prime')

x = 100
while x>1:
    x = x**0.5
    print(x)
'''
range(1)
for x in range(5):
    for y in range(x+1):
        print('*',end="")
    print("")