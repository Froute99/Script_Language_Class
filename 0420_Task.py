
from tkinter import *
from tkinter.ttk import *

import re


def stop(event=None):
    window.quit()


window = Tk()
window.title("Tkinter Assignment")
window.geometry("+0+0")
window.resizable(False, False)


wiki_python = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[30]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[34]
Python consistently ranks as one of the most popular programming languages.[35][36][37][38]'''


from tkinter.scrolledtext import ScrolledText


text = ScrolledText(width=50, height=10, font=('Arial', 10))
text.insert(END, wiki_python)
text.pack(padx=10, pady=10)

text.tag_configure('found', background='yellow', foreground='red')


option_frame = LabelFrame(text='Options')
option_frame.pack(pady=5)

ignore_case = BooleanVar()
ignore_case_button = Checkbutton(option_frame, text='Ignore case', variable=ignore_case)
ignore_case_button.pack()

founds = []

def select_pattern(event):
    global founds
    pattern = ''
    for i in history_listbox.curselection():
        # print(history_listbox.get(i))
        pattern = history_listbox.get(i)

    if ignore_case.get() is True:
        target = re.compile(pattern, re.IGNORECASE)
    else:
        target = re.compile(pattern)

    input_text = text.get("1.0", END)
    lines = input_text.splitlines()

    text.tag_remove('found', '1.0', END)
    for i, line in enumerate(lines):
        for mo in target.finditer(line):
            founds += [i, mo]
            text.tag_add('found', f'{i+1}.0+{mo.span()[0]}chars', f'{i+1}.0+{mo.span()[1]}chars')


def change_found_text(event=None):
    new_text = entry.get()
    for found in founds:
        text.replace(f'{found[0]+1}.0+{(found[1].span())[0]}chars', f'{found[0]+1}.0+{(found[1].span())[1]}chars', new_text)


entry = Entry(width=30)
entry.bind('<Return>', change_found_text)
entry.pack(pady=12)


history_listbox = Listbox(option_frame, selectmode='single', height=5)
history_listbox.insert(END, 'python')
history_listbox.insert(END, '[a-zA-Z]+')
history_listbox.pack()
history_listbox.bind('<<ListboxSelect>>', select_pattern)


window.bind('<Escape>', stop)

window.mainloop()
