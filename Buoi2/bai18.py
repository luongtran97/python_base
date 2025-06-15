# phuong trinh bac 2 ax** + bx +c = 0 , dk a!=0
from math import sqrt
# a = int(input('nhap a'))
# b = int(input('nhap b'))
# c = int(input('nhap c'))

a,b,c = eval(input('nhap so a ,b ,c '))

if a == 0:
    if b == 0 and c == 0:
        print('pt vo so nghiem')
    elif b == 0 and c != 0:
        print('pt vo  nghiem')
    else:
        res = -b/c 
        print('phuuong trinh bac  x= %.1f'  %res)
else:
    delta = b**2 - (4*a*c)
    if delta == 0:
        print('Pt co nghiem kep x= %.1f ' %(-b/(2*a)))
    elif delta < 0:
        print('Pt vo nghiem')
    else:
        print('Pt co 2 nghiem phan biet')
        print('x1 = %.1f ' % ((-b + sqrt(delta))/(2*a)))
        print('x2 = %.1f ' % ((-b - sqrt(delta))/(2*a)))
        
        
    
    


