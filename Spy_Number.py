n = int(input())
s = 0
s1 = 1
while n>0:
    a = n%10
    s+=a
    s1*=a
    n = n//10
if s==s1:
    print("Spy Number")
else:
    print("Not Spy Number")
    