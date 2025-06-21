nhac_arr = []
str= ''
# vong lap while true, lap vo han cho den khi co dieu kien dung, minh tu y set duoc
while True:
    the_loai = input('nhap the loai nhac , dung lai bam 0: ')
    if the_loai == "0":
        break
    nhac_arr.append(the_loai)
print('cac the loai nhac da nhap:', ', '.join(nhac_arr))

