so = int(input('nhap so can kiem tra'))
if so <2:
    print(so, ' khong phai la so nguyen to')
else:
    is_so_nguyen_to = True
    for i in range(2,so):
        if so % i == 0:
            is_so_nguyen_to=False
            break

    if is_so_nguyen_to:
        print(so, 'la so nguyen to')
    else:
        print(so, ' khong phai so nguyen to')