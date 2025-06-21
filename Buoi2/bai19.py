# bai toan luy tien
loai_xe = input('Nhập loại xe (4 hoặc 7): ')
quang_duong = float(input('quang duong di bao bao nhieu km'))
thoi_gian_cho  = int(input('cho trong bao lau'))
tien_cuoc = 0
tien_cho = 0


if loai_xe == '4':
    gia_mo_cua = 11000
    gia_30km = 17600
    gia_sau_30km = 14500
elif loai_xe == '7':
    gia_mo_cua = 12000
    gia_30km = 19600
    gia_sau_30km = 17100
else:
    print('vui long nhap dung loai xe')
    exit()

if quang_duong <= 0.5:
    tien_cuoc = gia_mo_cua
elif quang_duong <=30: 
    tien_cuoc = gia_mo_cua + (quang_duong - 0.5) * gia_30km
else :
    tien_cuoc = gia_mo_cua + (30 - 0.5) * gia_30km  + (quang_duong - 30) * gia_sau_30km

if thoi_gian_cho > 5:
    # tien_cuoc += (thoi_gian_cho - 5) * 750
    tien_cho = (thoi_gian_cho - 5 ) * 750
else:
    tien_cho = 0

print('tong tien cho cua ban la {:,} VND'.format(tien_cho))

print('tong tien cuoc cua ban la {:,} + {:,} = {:,}  VND'.format(tien_cuoc,tien_cho,tien_cuoc + tien_cho))
