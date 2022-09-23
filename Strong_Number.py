n = int(input())
s = 0
for i in str(n):
    m = 1
    for i in range(1,int(i)+1):
        m *=i
    s+=m
if int(n)==s:
    print("The number",n,'is a strong number')
else:
    print("The number",n,'is not a strong number')