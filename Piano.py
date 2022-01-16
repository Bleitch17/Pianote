import pygame
from Note import Note
from Key import Key


class Piano:
    surface_x_pos = 217
    surface_y_pos = 128

    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self, mixer, x, y):
        self.mixer = mixer
        self.x_pos = x
        self.y_pos = y

        self.surface = pygame.Surface((Piano.surface_x_pos, Piano.surface_x_pos))
        self.surface.fill((0, 0, 0))

        # Order matters!
        self.keys = [Key(19, 0, 18, 78, "c#", Piano.black),
                     Key(46, 0, 18, 78, "d#", Piano.black),
                     Key(100, 0, 18, 78, "f#", Piano.black),
                     Key(127, 0, 18, 78, "g#", Piano.black),
                     Key(154, 0, 18, 78, "a#", Piano.black),
                     Key(1, 1, 26, 126, "c", Piano.white),
                     Key(28, 1, 26, 126, "d", Piano.white),
                     Key(55, 1, 26, 126, "e", Piano.white),
                     Key(82, 1, 26, 126, "f", Piano.white),
                     Key(109, 1, 26, 126, "g", Piano.white),
                     Key(136, 1, 26, 126, "a", Piano.white),
                     Key(163, 1, 26, 126, "b", Piano.white),
                     Key(190, 1, 26, 126, "c", Piano.white),
                     Key(208, 0, 9, 78, "extra", Piano.black)]

    def is_pressed(self, mouse_x, mouse_y) -> bool:
        for key in self.keys:
            if key.is_pressed(mouse_x - self.x_pos, mouse_y - self.y_pos):
                return True
        return False

    def return_note(self) -> Note:
        return None

    def draw(self, screen):
        for key in self.keys:
            key.draw(self.surface)
        screen.blit(self.surface, (self.x_pos, self.y_pos))
