check_score = float(input('nhap vao diem trung binh'))
if check_score > 10 or check_score <0:
    print('dtb khong hop le')
elif check_score >= 8:
    print('loai gioi')
elif check_score >= 6.5 :
    print('loai kha')
elif check_score >= 5 :
    print('loai trung binh')
elif check_score >= 3.5 :
    print('loai yeu')
else:
    print('loai kem')