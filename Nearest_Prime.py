t = int(input())
for i in range (t):
    a = int(input())
    j = a        
    while 1 :
        n = j
        prime = True
        for i in range (2,j):
            if n % i == 0:
                prime = False
                break
        if prime == True:
            break
        else:
            j -=1    
    k = a      
    while a : 
        m = k
        prime = True
        for z in range (2,k):
            if m % z == 0:
                prime = False
                break
        if prime == True:
            break
        else:
            k +=1
    if abs(a-n) > abs(a-m):
        print(m)
    else:
        print(n)