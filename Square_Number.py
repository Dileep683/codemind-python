n = int(input())
for i in range (n):
    sq=i**2
    if sq==n:
        print('True')
        break
else:
    print('False')