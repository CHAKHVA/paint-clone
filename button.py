from settings import BLACK, init_font
import pygame

class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK, brush=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.brush = brush

    def draw(self, surface):
        if not self.brush:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 1)

            if self.text:
                button_font = init_font(18)
                text_surface = button_font.render(self.text, False, self.text_color)
                surface.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, self.y + self.height / 2 - text_surface.get_height() / 2))
        else:
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.width)

    def check_click(self, pos):
        x, y = pos
        if not self.brush:
            if (x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height):
                return True
            return False
        else:
            if (x > self.x - self.width and x < self.x + self.width and y > self.y - self.height and y < self.y + self.height):
                return True
            return False
