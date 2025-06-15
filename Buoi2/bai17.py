# phuong trinh bac nhat ax + b = 0
a = int(input('nhap a ')) 
b = int(input('nhap b ')) 
if a == 0 and b == 0:
    print('pt vo so nghiem')
elif a == 0 and b != 0:
    print('pt vo  nghiem')
else:
    res = -b/a 
    print('phuuong trinh bac  x= %.1f'  %res)