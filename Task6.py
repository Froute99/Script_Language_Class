
import re


phoneNumbers = ('(031) 8041 - 0550', '3533435', '34239872', '353 3435', '01034243424', '(031) - 8041 0123',
                '(010) - 333 - 4444', '010333344444', '010-3333-444', '010 333 3444', '3542 - 8795', '099 - 353 - 3435',
                '010 - 34 - 34554', '342498765')

localNumberList = ('02', '051', '053', '032', '062', '042', '052', '044',
                   '031', '033', '043', '041', '063', '061', '054', '055', '064', '010')

phone_re = re.compile(r'''
    (\(?\d{2,3}\)?)?
    \s*?-?\s*?
    (\d{3,4})
    \s*?-?\s*?
    (\d{4})
    ''', re.VERBOSE)


for number in phoneNumbers:
    mo = phone_re.search(number)

    local_digits = ""
    if mo is not None and mo.group(1) is not None:
        local_digits = re.sub("[()]", "", mo.group(1))

    if mo is None:
        print(f"{number} ---> Wrong Number")
    elif (mo.group(2) is None) or (mo.group(3) is None):
        print(f"{number} ---> Wrong Number")
    elif mo.group(1) is None:
        print(f"{number} ---> (010) {mo.group(2)} - {mo.group(3)}")
    elif local_digits not in localNumberList:
        print(f"{number} ---> Wrong Local Number")
    else:
        print(f"{number} ---> ({local_digits}) {mo.group(2)} - {mo.group(3)}")
