from goose import *
from text_graphics import *
import pygame


def keep_living(clock, goose, goose_buttons, goose_display, screen):
    running = True
    while running and goose.alive:
        for i in range(30):
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            if pressed[0]:
                for button in goose_buttons.buttons:
                    button.press(pos)
        goose.second_passed()
        goose_display.update()
        pygame.display.update()

    if not goose.alive:
        Label("Умер от недостатка заботы...", FONT, pygame.Rect(INDENT, DEATH_INDENT_VERTICAL, 0, 0),
              RED, ORANGE, 2*INDENT, DEATH_INDENT_VERTICAL, screen).show()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
