tong_thu_nhap = float(input('nhap tong so thu nhap'))
so_nguoi_phu_thuoc = int(input('so nguoi phu thuoc'))
giam_tru_ban_than = 132
giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 52.8
tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc
thu_nhap_chiu_thue = tong_thu_nhap - tong_giam_tru

if tong_thu_nhap < 0:
    print('vui long nhap lai')
    exit()

if thu_nhap_chiu_thue <= 60:
    thue_suat = 0.05
elif thu_nhap_chiu_thue <= 120:
    thue_suat = 0.10
elif thu_nhap_chiu_thue <= 216:
    thue_suat = 0.15
elif thu_nhap_chiu_thue <= 384:
    thue_suat = 0.20
elif thu_nhap_chiu_thue <= 624:
    thue_suat = 0.25
elif thu_nhap_chiu_thue <= 960:
    thue_suat = 0.30
else:
    thue_suat = 0.35



tien_thue = thu_nhap_chiu_thue * thue_suat
print(f"Số tiền giảm trừ: {tong_giam_tru:.2f} triệu đồng")
print(f"Thu nhập chịu thuế: {thu_nhap_chiu_thue:.2f} triệu đồng")
print(f"Thuế suất áp dụng: {int(thue_suat * 100)}%")
print(f"Số tiền thuế phải đóng: {tien_thue:.2f} triệu đồng")