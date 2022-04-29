
from tkinter import *
from tkinter.ttk import *

import re


def stop(event=None):
    window.quit()


window = Tk()
window.title("Hi")
window.geometry("640x480+480+120")
# window.resizable(False, False)

first_line_frame = Frame()
first_line_frame.pack()


label = Label(first_line_frame, text='Hello, Tkinter')
label.pack(side=LEFT)

def rotate():
    text = label.cget('text')
    text = text[1:] + text[0]
    label.configure(text=text)

def button_command():
    label.configure(text='Don\'t do that')
    print('pushed')


button = Button(first_line_frame, text='Hello', command=rotate, takefocus=False)
button.pack(side=RIGHT)


def change_label_text(event=None):
    new_text = entry.get()
    label.configure(text=new_text)


entry = Entry(width=30)
entry.bind('<Return>', change_label_text)
entry.pack()


wiki_python = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[34]

Python consistently ranks as one of the most popular programming languages.[35][36][37][38]'''


from tkinter.scrolledtext import ScrolledText


text = ScrolledText(width=50, height=10, font=('Arial', 10))
text.insert(END, wiki_python)
text.pack()

text.tag_configure('found', background='yellow', foreground='red')



ignore_case = IntVar()
checkbutton = Checkbutton(text='Ignore case', variable=ignore_case)
checkbutton.pack()

pattern_var = StringVar()


def select_pattern(event=None):
    print(history_listbox.curselection())

    pattern = ''
    for i in history_listbox.curselection():
        print(history_listbox.get(i))
        pattern = history_listbox.get(i)

    target = re.compile(pattern)

    input_text = text.get("1.0", END)
    lines = input_text.splitlines()

    text.tag_remove('found', '1.0', END)
    for i, line in enumerate(lines):
        for mo in target.finditer(line):
            print(mo)
            text.tag_add('found', f'{i+1}.0+{mo.span()[0]}chars', f'{i+1}.0+{mo.span()[1]}chars')




history_listbox = Listbox(selectmode='single', height=5)
history_listbox.insert(END, 'Python')
history_listbox.insert(END, '[a-zA-Z]+')
history_listbox.pack()
history_listbox.bind('<<ListboxSelect>>', select_pattern)



window.bind('<Escape>', stop)
# window.bind('<Control-x>', stop)

window.mainloop()
