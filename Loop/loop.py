# duyet qua dieu kien thi dung while
# i =1 
# while i <= 10:
#     print(i)
#     i +=1

# duyet qua mang dung for 
# rows = 5
# for i in range(1,rows +1):
#     for j in range(1, i+1):
#         print(j, end= ' ')
#     print('')
given_num = int(input('nhap so luong day so: '))
i = 1 
tong = 0 
while i <= given_num:
    tong += i
    i+=1
print('sum = ',tong)