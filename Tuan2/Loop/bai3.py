n = int(input('nhap n'))
# cac su dung range(start,stop,step)
if n <= 0:
   print('dieu kien n > 0')
   exit()
tong = 0
tong_chan = 0
# A tong cac so le nho hon hoac bang  n
for i in range(1,n,2):
   tong +=i
   print(f'tong so le lan luot la {i} + {tong - i} = {tong}')
# A tong cac so le nho hon hoac bang  n
for i in range(1,n):
   if i % 2 == 0:
    tong_chan +=i
    print(f'tong so chan lan luot la {i} + {tong_chan - i} = {tong_chan}')
#tich
tong_tich = 1
for i in range(1, n+1):
   tong_tich *=i
   print(f'tong tich tung buoc :{i}! =  {tong_tich}')
# tong tich chia het cho 3 
tich = 1
chia_het_3 = False 
for i in range(1,n+1):
   if i %3 == 0:
      chia_het_3 = True
      tich *= i
      print(f'tong thich chia het cho 3  {int( tich /i) } x  {i} =  {tich}')
