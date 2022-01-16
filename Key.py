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

    def is_pressed(self, x, y) -> bool:
        if self._rect.collidepoint(x, y):
            return True
        return False

    @property
    def rect(self):
        return self._rect
