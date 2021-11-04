quantity = int(input('How many numbers you want to show? > '))

f1 = 0
f2 = 1
print('0, 1', end='')
for i in range(quantity-2):
    f3 = f1 + f2
    print(",",f3, end='')
    f1 = f2
    f2 = f3