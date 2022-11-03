n = int(input())
s = [0,1]
for i in range(1,n+1):
    a= s[-2]+s[-1]
    s.append(a)
if n in s:
    print('True')
else:
    print('False')