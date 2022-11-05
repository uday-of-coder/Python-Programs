a,b,n = 0,1,0

while n < 5 :
    print(a+b)
    a,b = b,a+b
    n += 1
