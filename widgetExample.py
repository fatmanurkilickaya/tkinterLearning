from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

label= Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10, pady=10)
label.pack()

def button_clicked():
    my_entry=entry.get()
    print(my_entry)
    my_text = text.get("1.0",END)
    print(my_text)
    #1.0-> 1 = line , 0= character

#button
button = Button(text="button", command=button_clicked)
button.config(padx=10, pady=10)
button.pack()

#entry
entry = Entry(width=20)
entry.focus()
entry.pack()

#multiline text
text = Text(width=50, height=5)
#text.focus()
text.pack()

def scale_selected(value):
    print(value)

#scale
scale = Scale(from_= 0, to = 50, command= scale_selected)
scale.pack()

def spinbox_selected():
    print(spinbox.get())


#spinbox
spinbox = Spinbox(from_ =0, to=50,command=spinbox_selected)
spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
checkbutton.pack()

#radio_button
def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
radiobutton = Radiobutton(text="1. option", value=10, variable=radio_checked_state, command=radio_selected)
radiobutton2 = Radiobutton(text="2. option", value=15, variable=radio_checked_state, command=radio_selected)
radiobutton.pack()
radiobutton2.pack()

#listbox

def listbox_selected(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox()
name_list = ["Fatmanur", "nur", "Fat", "Nurkilickaya"]
#bana indexleri verir
for i in range(len(name_list)):
    print(i)
for i in range(len(name_list)):
    listbox.insert(i, name_list[i])
listbox.bind('<<ListboxSelect>>', listbox_selected)
listbox.pack()


window.mainloop()