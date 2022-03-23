
# 다음 시간 시험
# re = regular expression

import re


phone_re = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = phone_re.search('010-1234-5678')
mo.group(1)
mo.group(2)
mo.group(3)
mo.group(0)
mo.groups()

'''--------------------------------------'''

idol_re = re.compile(r'로제|제니')
mo = idol_re.search('로제와 제니')
mo.group()
mo = idol_re.search('제니와 로제와')
mo.group()


'''--------------------------------------'''

# 가운데 - 가 있어도 되고 없어도 됌
phone_re = re.compile(r'\d\d\d(-)?\d\d\d\d-\d\d\d\d')
phone_re.search('010---1234-5678')

# 별표는 있거나 여러개 있거나
phone_re = re.compile(r'\d\d\d(-)*\d\d\d\d-\d\d\d\d')
phone_re.search('0101234-5678')

# 3자리 또는 4자리
phone_re = re.compile(r'\d{3}-(\d){3,4}-\d{4}')
phone_re.search('010-1234-5678')
phone_re.search('010-123-5678')

# greedy 매칭 / ? 은 non-greedy
phone_re = re.compile(r'\d{3,5}?')
phone_re.search('12345678')


phone_re = re.compile(r'\d{3}-(\d){3,4}-\d{4}')
phone_re.findall('010-1234-5678 010-123-5678')


text = "Hello, World"

vowel_re = re.compile(r'[aeiouAEIOU]')
vowel_re.findall(text)

something_re = re.compile(r"[다]")
something_re.findall("감사합니다. 고맙습니다.")


idol_re = re.compile(r"^로제")
idol_re.search("로제는 사랑입니다.")
idol_re = re.compile(r"로제$")
idol_re.search("사랑은로제")

# . 은 무엇이든 뒤에 붙은 글자로 끝나는거 findall 다 붙인거 넣으면?
idol_re = re.compile(r".치")
idol_re = re.compile(r"..치")
idol_re.findall("가물치 참치 꽁치 쥐치")


