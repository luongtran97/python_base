so_n = int(input('nhap so n: '))
so_m = int(input('nhap so m: '))
if so_n <=0 or so_m <=0:
    print('vui long nhap lai')
    exit()

# for i  in range(11):
#     print(f'Kết quả {so_n} x {i} = {so_n * i}')
while so_n <= so_m:
    i = 1
    while i < 11:
        print(f'Kết quả {so_n} x {i} = {so_n * i}')
        i += 1 
    so_n += 1