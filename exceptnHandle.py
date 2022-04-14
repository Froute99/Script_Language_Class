# raise ValueError

# raise ValueError('too young')

# raise Exception

# raise Exception('this is error')

try:
    age = int(input('enter age:'))
    if age < 18:
        # raise Exception('Too Young')
        raise ValueError('Too Young')
# except ValueError as err:
#     print(err)
except Exception as err:
    # print('Unexpected:', err)
    print(f'{err=}, {type(err)=}')


def boxPrint(symbol, width, height):
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    boxPrint(sym, w, h)

# buggy.py