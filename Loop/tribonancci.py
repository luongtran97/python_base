tribo = int(input('nhap so luong day so tribo'))
tribo_arr = [0,0,1]

for i in range(3,tribo):
    tribo_res = tribo_arr[i-1] + tribo_arr[i-2] + tribo_arr[i-3]
    tribo_arr.append(tribo_res)

for i in range(tribo):
    print(tribo_arr[i])
