from tkinter import *

window = Tk()
window.title('mile to kilometer converter')
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


miles_num = Entry(width=6,)
miles_num.grid(column=1, row=1)


miles = Label(text="Miles")
miles.grid(column=2, row=1)

is_equal_to = Label(text="Is Equal To:")
is_equal_to.grid(column=0, row=2)

result = Label(text=0)
result.grid(column=1, row=2)

km = Label(text="Km")
km.grid(column=2, row=2)


def change_miles():
    miles_to_calculate = int(miles_num.get())
    miles_to_calculate *= 1.609
    result.config(text=int(miles_to_calculate))


calculate = Button(text="CALC!", command=change_miles)
calculate.grid(column=1, row=3)



window.mainloop()