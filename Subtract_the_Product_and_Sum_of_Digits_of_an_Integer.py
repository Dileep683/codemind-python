n = int(input())
s = 0
s1 = 1
while n>0:
    a = n%10
    s+=a
    s1*=a
    n = n//10
print(s1-s)