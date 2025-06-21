n = int(input('nhap n'))
if n < 0:
    print('nhap lai n')
else:
    for i in range(2,n+1):
        j = 1
        print(f'bang cuu chuong cua {i}')
        for j in range (1 , 11):
            print(f'{i} x {j} = {i * j}')
