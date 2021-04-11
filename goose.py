import time
from tkinter import *
import tkinter
from text_graphics import *

pygame.init()
pygame.mixer.init()
f = FONT = pygame.font.Font(None, 24)


class Characteristics:
    lvl = 5
    max_lvl = 10
    time_passed = 0

    def __init__(self, parameter_name_, upgrade_name_):
        self.parameter_name = parameter_name_
        self.upgrade_name = upgrade_name_

    def upgrade(self):
        if time.time() - self.time_passed > 0.75:
            self.lvl += 1.1
            self.lvl = min(self.lvl, 10.1)
            self.time_passed = time.time()


def draw_goose_renaming():
    root = Tk()
    root.geometry(str(RENAME_WIDTH) + "x" + str(RENAME_HEIGHT))
    root["bg"] = '#ffb259'  # orange colour
    root.title("Введите новое имя гуся")
    new_name = StringVar()
    enter_name = Entry(root, bg="#ffffff", bd=2, textvariable=new_name, width=15, font=("Arial Bold", 20),
                       justify='center')
    rename = tkinter.Button(root, text="Переименовать", height=1, width=15, font=("Arial Bold", 14),
                            command=root.destroy, justify='center')
    enter_name.place(x=150, y=30, anchor="c")
    rename.place(x=60, y=60)
    root.mainloop()
    return new_name.get()


class Goose:
    name = ""
    satiety = Characteristics("Сытость", "Покормить")
    cleanliness = Characteristics("Чистота", "Искупать")
    entertainment = Characteristics("Весёлость", "Поиграть")
    talk_out = Characteristics("Желание помолчать", "Поговорить")
    parameters = [satiety, cleanliness, entertainment, talk_out]
    alive = True

    def set_name(self, name_):
        self.name = name_

    def is_dead(self):
        for parameter in self.parameters:
            if parameter.lvl <= 0:
                self.alive = False

    def second_passed(self):
        for parameter in self.parameters:
            parameter.lvl -= 0.1
        self.is_dead()


def rename():
    text = draw_goose_renaming()
    pygame.display.set_caption("Гусь " + text)


class GooseButtons:
    def __init__(self, goose_, screen_):
        self.goose = goose_
        self.screen = screen_
        lower_row = BUTTON_TOP + BUTTON_HEIGHT + BUTTON_VERTICAL_DIST
        right_column = LEFT_INDENT + BUTTON_WIDTH + BUTTON_HORIZONTAL_DIST
        rectangles = [pygame.Rect((LEFT_INDENT, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)),
                      pygame.Rect((LEFT_INDENT, lower_row, BUTTON_WIDTH, BUTTON_HEIGHT)),
                      pygame.Rect((right_column, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)),
                      pygame.Rect((right_column, lower_row, BUTTON_WIDTH, BUTTON_HEIGHT))]
        self.buttons = []
        for i in range(len(self.goose.parameters)):
            lbl = Label(self.goose.parameters[i].upgrade_name, FONT, rectangles[i], DARK_GREY,
                        GREY, BUTTON_TITLE_HORIZONTAL, BUTTON_TITLE_VERTICAL, self.screen)
            self.buttons.append(Button(lbl, self.goose.parameters[i].upgrade, BUTTON_BORDER))
        rename_goose_rect = pygame.Rect((right_column, UPPER_INDENT, BUTTON_WIDTH, BUTTON_HEIGHT / 2))
        rename_goose_lbl = Label("Переименовать", FONT, rename_goose_rect, DARK_GREY, GREY,
                                 BUTTON_TITLE_HORIZONTAL / 2, BUTTON_TITLE_VERTICAL / 3, self.screen)
        rename_goose = Button(rename_goose_lbl, rename, BUTTON_BORDER)
        self.buttons.append(rename_goose)

    def show(self):
        for button in self.buttons:
            button.activate()


class GooseDisplay:
    def __init__(self, goose_, screen_):
        self.goose = goose_
        self.screen = screen_
        self.labels = []
        for i in range(len(self.goose.parameters)):
            self.labels.append(Label(self.goose.parameters[i].parameter_name, f,
                                     pygame.Rect(LEFT_INDENT, UPPER_INDENT + i*INDENT, 0, 0), DARK_GREY,
                                     ORANGE, 0, 0, self.screen))

    def show(self):
        for label in self.labels:
            label.show()

    def update(self):
        for i in range(len(self.labels)):
            self.labels[i].configure(self.goose.parameters[i].parameter_name + ": " +
                                     str(round(self.goose.parameters[i].lvl)))
