import pygame


class Key:
    def __init__(self, x, y, w, h, symbol, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.symbol = symbol
        self.color = color

        self._rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def is_pressed(self, x, y) -> bool:
        if self._rect.collidepoint(x, y):
            return True
        return False

    def get_symbol(self):
        return self.symbol

    def update_color(self, new_color):
        if self.symbol == "c" and self.color == (0, 0, 0):
            self.color = (0, 0, 0)
        else:
            self.color = new_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self._rect)

