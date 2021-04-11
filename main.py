from life import *
import pygame
import sys
from welcome import GooseCreation

if __name__ == "__main__":
    welcome_screen = GooseCreation()
    goose_name = welcome_screen.get_goose_name()
    if goose_name == "":
        sys.exit()

    goose = Goose()
    goose.set_name(goose_name)

    # creating main window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(ORANGE)
    pygame.display.set_caption("Гусь " + goose_name)
    clock = pygame.time.Clock()

    # setting graphics in main window
    goose_buttons = GooseButtons(goose, screen)
    goose_display = GooseDisplay(goose, screen)
    goose_buttons.show()
    goose_display.show()
    goose_img = pygame.image.load('goose.png')
    screen.blit(goose_img, pygame.Rect(GOOSE_INDENT_HORIZONTAL, GOOSE_INDENT_VERTICAL,
                                       GOOSE_SIZE, GOOSE_SIZE))
    pygame.display.update()

    keep_living(clock, goose, goose_buttons, goose_display, screen)
