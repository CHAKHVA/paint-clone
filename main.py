import pygame
import pygame.gfxdraw
from pygame.locals import *
from settings import *
from brush import Brush
from button import Button
import math
from math import atan2, tan
from math import sqrt

def get_color_button(x, y, color):
    return Button(x, y, 30, 30, color)

def draw_bg(surface, buttons):
    surface.fill(BACKGROUND_COLOR)
    pygame.draw.line(surface, BLACK, (0, 110), (pygame.display.get_window_size()[0], 110))
    for key, button in buttons.items():
        button.draw(surface)
    pygame.display.update()

def draw(surface, brush, current_pos, last_pos):
    pygame.draw.circle(surface, brush.color, last_pos, brush.size / 2.2)
    pygame.draw.line(surface, brush.color, last_pos, current_pos, brush.size)
    pygame.draw.circle(surface, brush.color, current_pos, brush.size / 2.2)
    pygame.display.update()

def main():
    # Initializing
    pygame.init()

    # Setting up clock
    clock = pygame.time.Clock()

    # Initializing Screen
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(NAME)

    brush = Brush(5, BLACK)
    buttons = {
        'black' : get_color_button(10, 10, BLACK),
        'white' : get_color_button(40, 10, WHITE),
        'red' : get_color_button(70, 10, RED),
        'green' : get_color_button(10, 40, GREEN),
        'blue' : get_color_button(40, 40, BLUE),
        'yellow' : get_color_button(70, 40, YELLOW),
        'orange' : get_color_button(10, 70, ORANGE),
        'brown' : get_color_button(40, 70, BROWN),
        'purple' : get_color_button(70, 70, PURPLE),
        'clear' : Button(110, 10, 100, 90, WHITE, 'CLEAR'),
        '5' : Button(300, 55, 5, 5, BLACK, brush=True),
        '10' : Button(400, 55, 10, 10, BLACK, brush=True),
        '15' : Button(500, 55, 15, 15, BLACK, brush=True),
        '20' : Button(600, 55, 20, 20, BLACK, brush=True),
        '25' : Button(700, 55, 25, 25, BLACK, brush=True),
        '30' : Button(800, 55, 30, 30, BLACK, brush=True),
    }

    draw_bg(surface, buttons)

    running = True
    clicked = False
    button_click = False
    while running:
        clock.tick(FPS)

        last_pos = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                for key, button in buttons.items():
                    if button.check_click(pygame.mouse.get_pos()):
                        if button.text == 'CLEAR':
                            draw_bg(surface, buttons)
                        elif button.brush:
                            brush.set_size(button.width)
                        else:
                            brush.set_color(button.color)
                        button_click = True
                if button_click == False:
                    clicked = True

            if event.type == MOUSEBUTTONUP:
                if clicked == True and button_click == False and last_pos[1] - brush.size / 2 > 110:
                    pygame.draw.circle(surface, brush.color, last_pos, brush.size / 2.2)
                    pygame.display.update()
                button_click = False
                clicked = False

            if event.type == MOUSEMOTION and clicked == True:
                current_pos = pygame.mouse.get_pos()
                if current_pos[1]  > 110 and last_pos[1] > 110:
                    draw(surface, brush, current_pos, last_pos)

    pygame.quit()

if __name__ == '__main__':
    main()