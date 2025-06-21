so = int(input('nhap mot so bat ki: '))
i= 0
so_chan =[]
so_le =[]
# while i <= so:
#     if  i % 2  == 0:
#        so_chan.append(i)
#     else:
#         so_le.append(i)
#     i+=1

for i in range (1,so):
     if i % 2 ==0:
        so_chan.append(i)
     else:
        so_le.append(i)

if so_chan or so_le:
        print(f'so chan: {so_chan}')
        print(f'so le:  {so_le}')
else:
      print('so khong hop le')
     
