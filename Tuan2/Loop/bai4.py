x = int(input('nhap x '))
y = int(input('nhap y '))

tong_bp = 0

if x == 0 or y == 0:
    if x == 0:
        print('vui long nhap x != 0')
    else:
        print('vui long nhap y !=0')
else:
    if x < y:
        for i in range(x,y+1):
            tong_bp += i ** 2
        print('tong binh phuong la', tong_bp)
    else:
        print('gia tri x phai nho hon y de thuc hien vong lap')