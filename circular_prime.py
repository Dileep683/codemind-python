n = int(input())
p = 1
for i in range(2,n):
    if n % i == 0:
        p = 0
if p == 1 and n !=1:
    n = str(n)
    s = n[::-1]
    s = int(s)
    q = 1
    for j in range (2,s):
        if s%j ==0:
            q = 0
    if q ==1:
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
        
    
    