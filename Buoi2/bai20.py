# tinh tien dien
so_dien = int(input('nhap so dien KWh tieu thu: '))
tien_dien = 0
if so_dien <=0:
    print('so dien khong hop le')
    exit()
elif so_dien <=50:
    tien_dien = so_dien * 1678
elif so_dien <=100:
    tien_dien = 50 *1678 + (so_dien - 50) * 1734   
elif so_dien <=200:
    tien_dien = 50 * 1678 + 50 * 1734 + (so_dien - 100) * 2014  
elif so_dien <=300:
    tien_dien = 50* 1678 + 50 * 1734 + 100 * 2014 + (so_dien - 200) * 2536   
elif so_dien <=400:
    tien_dien = 50* 1678 + 50 * 1734 + 100 * 2014 +  100 * 2536 + (so_dien-300)  * 2834   
else:
    tien_dien = 50* 1678 + 50 * 1734 + 100 * 2014 +  100 * 2536 +  100*2834  +  (so_dien-400)  * 2927   

print('so tien dien cua ban la: {:,} '.format(int(tien_dien)) , 'vnd')