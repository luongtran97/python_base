num = int(input('kiem tra so hoan hao: '))
# so hoan hao
# uoc_so = []
# check_num = 0
# for i in range (1,num+1):
#     if num % i == 0 and i < num:
#         uoc_so.append(i)
# for i in uoc_so:
#     check_num += i

# if check_num == num:
#      print(f'{num} la so hoan hao')
# else:
#     print(f'{num} khong phai la so hoan hao')


# cach 2 
tong_uoc = 0

for i in range(1,num):
    if num % i == 0:
        tong_uoc += i

if tong_uoc == num:
     print(f'{num} la so hoan hao')
else:
    print(f'{num} khong phai la so hoan hao')