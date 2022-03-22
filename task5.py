
import keyboard
import pyperclip
import winsound

def report():
    winsound.Beep(500, 200)
    winsound.Beep(500, 200)
    keyboard.write('shift+windows+w is pressed')


keyboard.add_hotkey('shift+windows+w', report)

string = pyperclip.paste()
#splited = string.replace(',', '').split()
wordList = string.replace(',', '').split()
wordCount = {}

for word in wordList:
    if word.isalpha():
        wordCount[word] = wordCount.get(word, 0) + 1
keys = sorted(wordCount.keys())

# 출력부
for word in keys:
    print(word + ':' + str(wordCount[word]))


