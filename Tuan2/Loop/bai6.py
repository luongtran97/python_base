# tim uoc chung lon nhat
a = int(input('nhap a'))
b = int(input('nhap b'))
uoc_a =[]
for i in range(1,a+1):
    if  a % i == 0:
        uoc_a.append(i)

uoc_b =[]

for i in range(1,b+1):
    if  b % i  == 0:
        uoc_b.append(i)


ucln = 1
for i in uoc_a:
    if i in uoc_b and i > ucln:
        ucln = i
print('uoc chung lon nhat la:', ucln)