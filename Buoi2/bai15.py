prd_name = input('name product?')
prd_qty = int(input('qty product?'))
prd_price = int(input('product price?'))
check_discount = prd_qty * prd_price 
if check_discount > 130000:
    print('san pham' ,prd_name , 'ban duoc giam gia 10% {:,}' .format(check_discount * 0.9) )
else:
    print('tong gia tien chua du dieu kien giam gia')    