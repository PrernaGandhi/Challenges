import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(padx=30,pady=30)
# this is going to place the label on the screen
# without this we won't be able to see the label
# side = "bottom", "left", "right", "top" decides the position of the label
# my_label.pack(side="bottom")
# expand true means it is going to try to take the entire screen size
# my_label.pack(expand=True)
# my_label.pack()
# use place with coordinates
# my_label.place(x=0, y=0)
# we can't mix and match pack and grid in the same program
my_label.grid(row=0,column=0)

# my_label["text"] = "New Text"
# my_label.config(text="Config new text")


# make label text button clicked when button got clicked
def button_clicked():
    my_label.config(text=user_input.get())


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(row=1,column=1)
# user input
user_input = tkinter.Entry(width=10)
# user_input.pack()
user_input.grid(row=2,column=2)
print(user_input)
print(user_input.get())

# Entries
entry = tkinter.Entry(width=30)
# Add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
# entry.pack()

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
# text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
window.mainloop()
