def proper_fractor(num):
    pfs = 0
    for i in range (1,num):
        if num % i == 0:
            pfs += i
    return pfs
a = int(input())
b = int(input())
if proper_fractor(a) == b and proper_fractor(b) == a:
    print('Amicable')
else:
    print('Not Amicable')