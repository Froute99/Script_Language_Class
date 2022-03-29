

import re


phone_re = re.compile(r'''
    ^
    (
        (010|02|051|053)            # 괄호가 없는 국번
        |
        (\(
            [ ]*
            (010|02|051|053)        # 괄호가 있는 국번
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
''', re.VERBOSE)

good_str = [
    '(02)12345678', '0212345678', '010-1234-1234',
    '( 02 ) 1234  1234', '12345678'
]

bad_str = [
    '(02 1234 5678', '01 1234 1234', '999 12345 1234',
    '(0 2) 1234 1234', '( 05 1) 1234 1234 ', '(02 4444 - 4444',
    '010-1234-55555', '010 1234 55555'
]


def test_good():
    for s in good_str:
        mo = phone_re.search(s)
        if not mo:
            print('Good Case Failure')
            print(s)


def test_bad():
    for s in bad_str:
        mo = phone_re.search(s)
        if mo:
            print('Bad Case Failure')
            print(mo)


def test():
    test_good()
    test_bad()

test()


password_re = re.compile(r'[a-zA-Z]{10,}')  # 영문자 10자 이상
password_re = re.compile(r'[a-zA-Z0-9]{10,}')  # 영문자숫자조합 10자이상


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


import exrex

good_number_list = []

for i in range(1000):
    random_phone = exrex.getone(final_pattern, 2)
    good_number_list += [random_phone]
