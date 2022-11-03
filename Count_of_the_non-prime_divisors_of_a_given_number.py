n = int(input())
s = 1
for i in range (1,n+1):
    if n % i == 0:
        p = 0
        for j in range (2,i):
            if i%j == 0:
                p = 1
        if p == 1:
            s+=1
print(s)
            
        
        