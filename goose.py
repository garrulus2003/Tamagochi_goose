import time

import self as self

from sizes import *
from text_graphics import *


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
