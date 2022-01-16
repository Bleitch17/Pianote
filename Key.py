import pygame


class Key:
    pressed_color = (150, 150, 150)

    def __init__(self, x, y, w, h, symbol, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.symbol = symbol
        self.color = color

        self._rect = pygame.Rect(x, y, w, h)
        self.pressed = False

    def is_pressed(self, x, y) -> bool:
        if self._rect.collidepoint(x, y):
            self.pressed = True

            return self.pressed
        self.pressed = False
        return self.pressed

    @property
    def rect(self):
        return self._rect
