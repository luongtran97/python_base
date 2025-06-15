money = int(input('nhap so tien can doi'))
so_to_500 = money // 500000
money %=  500000 
so_to_200 = money // 200000 
money %= 200000  
so_to_100 = money // 100000 
money %= 100000  
so_to_50 = money // 50000 
money %= 50000  

print('so to 500k', so_to_500)
print('so to 200k', so_to_200)
print('so to 100k', so_to_100)
print('so to 50k', so_to_50)
print('so tien con lai {:,} ' .format(money) )
