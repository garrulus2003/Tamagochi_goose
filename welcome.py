from tkinter import *
from sizes import *


class GooseCreation:
    # setting a welcome screen
    def set_goose(self):  # returns the name of a goose entered
        self.root.destroy()

    def create_goose(self):  # sets a screen with a window to enter the name
        for w in self.root.winfo_children():
            if w.winfo_class() == 'Button':
                w.place_forget()
        self.lbl.configure(text="Придумай гусю имя:")
        self.lbl.place(x=70, y=150)
        self.enter_name.place(x=200, y=250, anchor="c")
        self.create_goose_b.place(x=112, y=300)

    def not_creating_goose(self):  # sets a sad screen which invites to create a goose
        self.lbl.configure(text="А зря, гуси классные...")
        self.btn_no.destroy()
        self.btn_yes.destroy()
        self.btn_though.place(x=110, y=250)

    def __init__(self):
        self.root = Tk()
        self.root.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.root["bg"] = '#ffb259'  # orange colour
        self.root.title("Тамагочи-гусь")
        self.lbl = Label(self.root, text="Привет! \n Хочешь завести гуся?", bg='#ffb259', font=("Arial Bold", 20))
        self.lbl.place(x=60, y=150)
        self.goose_name = StringVar()
        self.enter_name = Entry(self.root, bg="#ffffff", bd=2, textvariable=self.goose_name, width=14, font=("Arial Bold", 20),
                                justify='center')
        self.create_goose_b = Button(self.root, text="Создать!", height=2, width=15, font=("Arial Bold", 14),
                                     command=self.set_goose)

        self.btn_though = Button(self.root, text="Всё-таки завести!", height=2, width=15, font=("Arial Bold", 14),
                                 command=self.create_goose)

        self.btn_yes = Button(self.root, text="Да!", height=2, width=7, font=("Arial Bold", 14),
                              command=self.create_goose)
        self.btn_no = Button(self.root, text="Нет...", height=2, width=7, font=("Arial Bold", 14),
                             command=self.not_creating_goose)
        self.btn_yes.place(x=100, y=300)
        self.btn_no.place(x=210, y=300)

    def get_goose_name(self):
        self.root.mainloop()
        return self.goose_name.get()
