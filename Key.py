import pygame


class Key:
    def __init__(self, x, y, w, h, symbol, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.symbol = symbol
        self.color = color

        self.draw_color = color

        self._rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.pressed = False

    def is_pressed(self, x, y) -> bool:
        if self._rect.collidepoint(x, y):
            self.pressed = True
            print(f"Key pressed: {self.symbol}")
            return self.pressed
        self.pressed = False
        return self.pressed

    def update_color(self, new_color):
        self.color = new_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self._rect)

    @property
    def rect(self):
        return self._rect
