from colours import *
import pygame


class Label:
    """
    The Label class.

    Attributes
    -------
    typeface : pygame font
    rect : pygame rectangle
    colour : (int, int, int)
    root : pygame screen
        rgb colour of text
    bg : (int, int, int)
        rgb colour for background
    text : str
    indent_x : int
        vertical indent
    indent_y : int
        horizontal indent

    Methods
    -------
    show():
        prints the text on the screen
    show_border():
        shows border if needed
    hide():
        hides the text
    configure():
        changes the text on the screen

    """
    def __init__(self, text_, typeface_, rect_, colour_, bg_, indent_x_, indent_y_, root_):
        self.typeface = typeface_
        self.rect = rect_
        self.colour = colour_
        self.bg = bg_
        self.text = text_
        self.indent_x = indent_x_
        self.indent_y = indent_y_
        self.root = root_

    def show(self):
        pygame.draw.rect(self.root, self.bg, self.rect)
        self.root.blit(self.typeface.render(self.text, True, self.colour), (self.rect.x + self.indent_x,
                                                                            self.rect.y + self.indent_y))
        pygame.display.update()

    def show_border(self, border_colour, width):
        pygame.draw.rect(self.root, border_colour, self.rect, width)
        pygame.display.update()

    def hide(self):
        self.root.blit(self.typeface.render(self.text, True, self.bg), (self.rect.x + self.indent_x,
                                                                        self.rect.y + self.indent_y))
        pygame.display.update()

    def configure(self, new_text):
        self.hide()
        self.text = new_text
        self.show()


class Button:
    """
    The Button class.

    Attributes
    -------
    btn_label : Label
        the button and the text printed
    btn_function : function
        the functions which is activated when the button id pressed
    border_width : int
    border_colour : (int, int, int)
        rgb colour of the border
    active : bool
        whether the button is activated

    Methods
    -------
    activate():
        show the button and make it active
    deactivate()
    press(pygame pos):
        execute the function if the button is pressed
    """
    active = False

    def __init__(self, btn_label_, btn_function_, border_width_=1, border_colour_ =DARK_GREY):
        self.btn_label = btn_label_
        self.btn_function = btn_function_
        self.border_width = border_width_
        self.border_colour = border_colour_

    def activate(self):
        self.btn_label.show()
        self.btn_label.show_border(self.border_colour, self.border_width)
        self.active = True

    def deactivate(self):
        self.active = False

    def press(self, pos):
        if self.active and self.btn_label.rect.collidepoint(pos):
            self.btn_function()

