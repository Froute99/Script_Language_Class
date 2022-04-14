# import traceback
#
#
# def bacon():
#     try:
#         raise Exception('Error')
#     except:
#         ef = open('error_stack.txt', 'w')
#         for line in traceback.format_stack():
#             ef.write(line)
#         ef.close()
#
#
# def spam():
#     bacon()
#
#
# spam()

data = 100

assert data == 100

assert data < 100

age = input('Enter Age: ')
assert type(age) is int, "age should be integer"

