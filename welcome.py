from tkinter import *
from sizes import *


def welcome():
    # setting a welcome screen
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root["bg"] = '#ffb259'  # orange colour
    root.title("Тамагочи-гусь")
    lbl = Label(root, text="Привет! \n Хочешь завести гуся?", bg='#ffb259', font=("Arial Bold", 20))
    lbl.place(x=60, y=150)

    def set_goose():  # returns the name of a goose entered
        root.destroy()

    def create_goose():  # sets a screen with a window to enter the name
        for w in root.winfo_children():
            if w.winfo_class() == 'Button':
                w.place_forget()
        lbl.configure(text="Придумай гусю имя:")
        lbl.place(x=70, y=150)
        enter_name.place(x=200, y=250, anchor="c")
        create_goose_b.place(x=112, y=300)

    def not_creating_goose():  # sets a sad screen which invites to create a goose
        lbl.configure(text="А зря, гуси классные...")
        btn_no.destroy()
        btn_yes.destroy()
        btn_though.place(x=110, y=250)

    # buttons and labels
    goose_name = StringVar()
    enter_name = Entry(root, bg="#ffffff", bd=2, textvariable=goose_name, width=14, font=("Arial Bold", 20),
                       justify='center')
    create_goose_b = Button(root, text="Создать!", height=2, width=15, font=("Arial Bold", 14),
                            command=set_goose)

    btn_though = Button(root, text="Всё-таки завести!", height=2, width=15, font=("Arial Bold", 14),
                        command=create_goose)

    btn_yes = Button(root, text="Да!", height=2, width=7, font=("Arial Bold", 14),
                     command=create_goose)
    btn_no = Button(root, text="Нет...", height=2, width=7, font=("Arial Bold", 14),
                    command=not_creating_goose)

    btn_yes.place(x=100, y=300)
    btn_no.place(x=210, y=300)

    root.mainloop()

    return goose_name.get()