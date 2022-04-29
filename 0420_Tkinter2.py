from tkinter import *
from tkinter.ttk import *


def stop(event=None):
    window.quit()


window = Tk()
window.title("tkinter practice")
# window.geometry("640x480+0+0")
window.geometry("+0+0")
window.resizable(False, False)
window.bind('<Escape>', stop)


def enter_new_pattern(event=None):
    new_pattern = combobox.get()
    main_text.insert('1.0', f'new pattern \"{new_pattern}\" is entered\n')
    print(combobox['values'])
    combobox['values'] += (new_pattern, )


combo_frame = LabelFrame(text='Pattern')
combo_frame.pack(fill=BOTH, padx=5, pady=5)

combobox = Combobox(combo_frame, values=['Python', '[a-zA-Z]+'])
combobox.bind('<Return>', enter_new_pattern)
combobox.pack(fill=BOTH, padx=5, pady=5)




text_frame = LabelFrame(text='LOG')
text_frame.pack(padx=10, pady=10)

from tkinter.scrolledtext import ScrolledText
source_text = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code
readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help
programmers write clear, logical code for small- and large-scale projects.[30]
'''

main_text = ScrolledText(text_frame)
# main_text.insert(END, source_text)
main_text.pack()


command_frame = LabelFrame(text='Command')
command_frame.pack(fill=BOTH, padx=10, pady=10)


from tkinter import filedialog

def open_file():
    # 1개만
    file_name = filedialog.askopenfilename(title='Select a text file', filetypes=((".txt files", "*.txt"), ("all files", "*.*")))
    # 2개만
    # file_names = filedialog.askopenfilenames(title='Select text files', filetypes=(("text files (.txt)", "*.txt"), ("all files", "*.*")))
    # print(file_names)
    print(file_name)
    main_text.insert('1.0', f'file {file_name} is selected\n')
    pass


def command_a():
    main_text.delete('1.0', END)
    pass

def command_b():
    # main_text.insert(END, source_text)
    main_text.insert('1.0', f'current pattern is {combobox.get()}\n')
    pass

def command_c():
    # main_text.replace('1.0', '1.6', 'PYTHON PYTHON')
    open_file()
    pass

def command_d():
    pass


Button(command_frame, command=command_a, text='Command A').pack(side=LEFT, expand=True, fill=BOTH, padx=5)
Button(command_frame, command=command_b, text='Command B').pack(side=LEFT, expand=True, fill=BOTH, padx=5)
Button(command_frame, command=command_c, text='Command C').pack(side=LEFT, expand=True, fill=BOTH, padx=5)
Button(command_frame, command=command_d, text='Command D').pack(side=LEFT, expand=True, fill=BOTH, padx=5)






menu = Menu()
menu_file = Menu(menu, tearoff=False)
menu_file.add_command(label='Open', accelerator='Ctrl + O')
menu_file.add_command(label='Save File', accelerator='Ctrl + S', state='disable')
menu_file.add_separator()
menu_file.add_command(label='Quit', accelerator='Ctrl+Q')

menu.add_cascade(label='File', menu=menu_file)

menu_edit = Menu(menu, tearoff=False)
menu_edit.add_command(label='Open', accelerator='Ctrl + O')
menu_edit.add_command(label='Save File', accelerator='Ctrl + S', state='disable')
menu_edit.add_separator()
menu_edit.add_command(label='Quit', accelerator='Ctrl+Q')

menu.add_cascade(label='Edit', menu=menu_edit)

window.configure(menu=menu)

window.mainloop()



