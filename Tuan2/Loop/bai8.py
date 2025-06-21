prime = int(input('kiem tra so nguyen to: '))

if prime < 2:
    print(f'{prime} day khong phai la so nguyen to')
    exit()
is_prime = True
for i in range(2,prime):
    if prime % i == 0:
        is_prime = False
        break


# i = 2
# while i < prime:
#     if prime % i == 0:
#         is_prime = False
#         break
#     i += 1

# if is_prime:
#     print(f'{prime} la so nguyen to')
# else:
#     print(f'{prime} khong phai la  so nguyen to')
