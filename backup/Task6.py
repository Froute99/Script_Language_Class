
import re

phoneNumbers = ('(031) 8041 - 0550', '3533435', '34239872', '353 3435', '01034243424', '(031) - 8041 0123',
                '(010) - 333 - 4444', '010333344444', '010-3333-444', '010 333 3444', '3542 - 8795', '099 - 353 - 3435',
                '010 - 34 - 34554', '342498765')


localNumberList = ('02', '051', '053', '032', '062', '042', '052', '044',
                   '031', '033', '043', '041', '063', '061', '054', '055', '064', '010'
                   '(02)', '(051)', '(053)', '(032)', '(062)', '(042)', '(052)', '(044)',
                   '(031)', '(033)', '(043)', '(041)', '(063)', '(061)', '(054)', '(055)', '(064)', '(010)')
testNumber = r'(031) 8041 - 0550'


def compile_phone_number_re(phoneNumber):
    phone_number_re = re.compile(r'''
        (\d{2,3}|\(\d{2,3}\))?
        [\s]*?
        [-|.]?
        [\s]*?
        (\d{3,4})
        [\s]*?
        [-|.]?
        [\s]*?
        (\d{4})''', re.VERBOSE)
    return phone_number_re.search(phoneNumber)


def test_and_print(matchedObject):
    if (matchedObject is None) or (matchedObject.group(1) is None):
        print("Wrong Number")
    elif matchedObject.group(1) not in localNumberList:
        print("Wrong local number")
    else:
        print(f'({matchedObject.group(1)}) {matchedObject.group(2)} - {matchedObject.group(3)}')


for number in phoneNumbers:
    mo = compile_phone_number_re(number)
    test_and_print(mo)


#test_and_print(compile_phone_number_re(testNumber))

