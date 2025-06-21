n = int(input('nhap n'))

if n <= 0:
    print('vui long nhap lai n : ')
    exit()
# i=0
# while i < n:
#     print( n - i  )
#     i +=1

for i in range(n):
    print(n-i)