
text = """
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[34]
"""

word_list = text.split()
word_list = [word for word in word_list if word.isalpha()]
count = {}
for word in word_list:
    count.setdefault(word, 0)
    count[word] += 1


print('Word Count'.center(30, '='))
for key, value in count.items():
    print(key.ljust(19), f'{value:10}')



'''
import keyboard
import pyperclip
import winsound

def report():
    winsound.Beep(500, 200)
    winsound.Beep(500, 200)
    keyboard.write('shift+windows+w is pressed')


keyboard.add_hotkey('shift+windows+w', report)

string = pyperclip.paste()
wordList = string.replace(',', ' ').split()
wordCount = {}

for word in wordList:
    if word.isalpha():
        wordCount[word] = wordCount.get(word, 0) + 1
keys = sorted(wordCount.keys())

# 출력부
for word in keys:
    print(word + ':' + str(wordCount[word]))
'''

