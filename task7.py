
import exrex
import re

pattern = r'''
    ^
    (
        (010|02|051|053)
        |
        (\(
            [ ]*
            (010|02|051|053)
            [ ]*
        \))
        [ ]*
        -?
        [ ]*
    )?
    [ ]*
    \d{3,4}
    [ ]*
    -?
    [ ]*
    \d{4}
    $
'''

final_pattern = re.sub(r'[ ]{2,}|\t|\n', '', pattern)

good_number_list = []

for i in range(1000):
    random_phone = exrex.getone(final_pattern, 2)
    good_number_list += [random_phone]

phone_re = re.compile(r'''
    (\(?\d{2,3}\)?)?
    \s*?-?\s*?
    (\d{3,4})
    \s*?-?\s*?
    (\d{4})
    ''', re.VERBOSE)


result = []

for s in good_number_list:
    mo = phone_re.search(s)
    if not mo:
        print(s)
        result += [s]
