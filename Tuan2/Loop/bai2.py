chuoi = input('nhap chuoi  ')
print("Các ký tự trước khoảng trắng đầu tiên: ")
i = 0
for  ky_tu in chuoi:
    if ky_tu == ' ':
        print('vi tri khoang trang dau tien la: ', i)
        break
    print(ky_tu, end = '')
    i +=1 

for  ky_tu in chuoi:
    if ky_tu != ' ':
        print(ky_tu)

if 'a' in chuoi:
    print('co ki tu a trong chuoi')
else:
    print('khong co ky tu a trong chuoi')
