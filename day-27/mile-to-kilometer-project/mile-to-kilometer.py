import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=30,pady=30)


def calculate_kms():
    km.config(text=f"{round(float(mile.get()) * 1.609, 2)}")


mile = tkinter.Entry(width=10)
mile.grid(row=0, column=1)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km = tkinter.Label(text="0", width=10)
km.grid(row=1, column=1)

km_label = tkinter.Label(text="Kms")
km_label.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=calculate_kms)
button.grid(row=2,column=1)



window.mainloop()