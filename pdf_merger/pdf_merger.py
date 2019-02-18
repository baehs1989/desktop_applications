from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from PyPDF2 import PdfFileMerger
import os


def swap(arr, i1, i2):
    start = 0
    end = len(arr) - 1

    if not start <= i1 <= end or not start <= i2 <= end:
        return False

    temp = arr[i2]
    arr[i2] = arr[i1]
    arr[i1] = temp

    return True

def file_save():
    files = list(listbox1.get(0, END))

    if len(files) == 0:
        messagebox.showinfo("Error", "Please select files to merge.")

    else:

        merger = PdfFileMerger()

        for file in files:
            merger.append(open(file, 'rb'))

        with filedialog.asksaveasfile(mode='wb', defaultextension='.pdf') as fout:
            merger.write(fout)

def browse_file():
    filenames = filedialog.askopenfilenames(filetypes=[("PDF file(s)", "*.pdf")])
    # print (filenames)
    for file in filenames:
        listbox1.insert(END,file)


def delete_from_listbox():
    try:
        start = selected_rows[0]

        files = listbox1.get(0,END)

        files = [file for i,file in enumerate(files) if i not in listbox1.curselection()]

        listbox1.delete(0,END)

        for file in files:
            listbox1.insert(END,file)

        listbox1.selection_set(start)

    except:
        pass


def get_selected_rows(event):
    try:
        global selected_rows
        selected_rows = listbox1.curselection()
        # print (selected_rows)
    except:
        pass

def move_top():
    try:
        files = listbox1.get(0,END)
        moved_files = []
        temp_files = []

        for i, file in enumerate(files):
            if i not in list(listbox1.curselection()):
                temp_files.append(file)
            else:
                moved_files.append(file)

        listbox1.delete(0,END)
        for file in moved_files + temp_files:
            listbox1.insert(END,file)

        listbox1.selection_set(0,len(moved_files)-1)
    except:
        pass


def move_up():
    try:
        files = list(listbox1.get(0, END))
        selected_file = list(listbox1.curselection())

        moved_index = []
        for i in selected_file:
            if i-1 not in moved_index:
                if swap(files, i, i-1):
                    moved_index.append(i-1)
                else:
                    moved_index.append(i)
            else:
                moved_index.append(i)

        listbox1.delete(0,END)
        for file in files:
            listbox1.insert(END,file)

        for i in moved_index:
            listbox1.selection_set(i)

    except:
        pass


def move_down():
    try:
        files = list(listbox1.get(0, END))
        selected_file = reversed(list(listbox1.curselection()))

        moved_index = []
        for i in selected_file:
            if i+1 not in moved_index:
                if swap(files, i, i+1):
                    moved_index.append(i+1)
                else:
                    moved_index.append(i)
            else:
                moved_index.append(i)

        listbox1.delete(0,END)
        for file in files:
            listbox1.insert(END,file)

        for i in moved_index:
            listbox1.selection_set(i)

    except:
        pass


def move_bottom():
    try:
        files = listbox1.get(0,END)
        moved_files = []
        temp_files = []

        for i, file in enumerate(files):
            if i not in list(listbox1.curselection()):
                temp_files.append(file)
            else:
                moved_files.append(file)

        listbox1.delete(0,END)
        for file in temp_files + moved_files:
            listbox1.insert(END,file)

        listbox1.selection_set(len(temp_files + moved_files) - len(moved_files), END)
        # listbox1.selection_set(0)
        # listbox1.selection_set(4)

        # print (listbox1['width'])

    except:
        pass

def window_resized(event):
    # print (event.x)
    # print (event.width, event.height)
    if event.x == 5:
        listbox1.config(width=int(event.width*0.065), height=int(event.height*0.045))

def do_about_dialog():
    tk_version = window.tk.call('info', 'patchlevel')
    messagebox.showinfo(message= app_name + "\nMerging PDF files.\n\nTK version: " + tk_version)



app_name="PDF Merger v1.0"

window = Tk()
window.title(app_name)
window.configure(padx=20,pady=20)

window.geometry("530x280")
window.bind('<Configure>', window_resized)
# window.resizable(0,0)

#========================Menu Bar==============================
menubar = Menu(window)
app_menu = Menu(menubar, name='apple')
menubar.add_cascade(menu=app_menu)

tk_version = window.tk.call('info', 'patchlevel')
tk_version = tk_version.replace('.', '')
tk_version = tk_version[0:2]
tk_version = int(tk_version)

app_menu.add_command(label='About ' + app_name, command=do_about_dialog)
app_menu.add_separator()

# if tk_version < 85:
#     app_menu.add_command(label="Preferences...", command=do_preferences)
# else:
#     # Tk 8.5 and up provides the Preferences menu item
#     window.createcommand('tk::mac::ShowPreferences', do_preferences)

window.config(menu=menubar)
#==============================================================




#=========================Scroll bar===========================
sb1=Scrollbar(window)
sb1.grid(row=1,column=4,rowspan=6, padx=10)
#==============================================================





#==========================List Box============================
listbox1 = Listbox(window, selectmode=EXTENDED, height=10, width=35)
listbox1.grid(row=0,column=0, rowspan=6, columnspan=4, sticky='nsew')

listbox1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox1.yview)

listbox1.bind('<<ListboxSelect>>', get_selected_rows)
#==============================================================





#=========================Label Frame==========================

labelframe2 = LabelFrame(window, text='', pady=12, padx=7, borderwidth=0)
labelframe2.grid(row=0,column=5, rowspan=6)

labelframe = LabelFrame(labelframe2, text="move selected file")
#==============================================================






#==========================Buttons===============================
button_cnf={'width':10}
button_margin={'pady':2}

b1 = Button(labelframe2, text="Add file(s)", cnf=button_cnf, command=browse_file)
# b1.grid(row=0, column=5)
b1.pack(cnf=button_margin)

b7 = Button(labelframe2, text="Delete file", cnf=button_cnf, command=delete_from_listbox)
# b7.grid(row=1, column=5)
b7.pack(cnf=button_margin)


b2 = Button(labelframe, text="top", cnf=button_cnf, command=move_top)
b2.pack(cnf=button_margin)

b3 = Button(labelframe, text="up", cnf=button_cnf, command=move_up)
b3.pack(cnf=button_margin)

b4 = Button(labelframe, text="down", cnf=button_cnf, command=move_down)
b4.pack(cnf=button_margin)

b5 = Button(labelframe, text="bottom", cnf=button_cnf, command=move_bottom)
b5.pack(cnf=button_margin)

labelframe.pack()

b6 = Button(window, text="Merge", width=25, cnf=button_cnf, command=file_save)
b6.grid(row=7, column=0, columnspan=6, pady=(10,0))

#=================================================================


window.mainloop()