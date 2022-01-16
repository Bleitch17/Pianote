import pygame
from Note import Note
from Key import Key


class Piano:
    black = (0, 0, 0)
    white = (255, 255, 255)
    pressed_color = (150, 150, 150)


    def __init__(self, mixer, x, y, scale):
        self.mixer = mixer
        self.x_pos = x
        self.y_pos = y
        self.scale_factor = scale

        self.surface = pygame.Surface((217 * self.scale_factor, 128 * self.scale_factor))
        self.surface.fill((0, 0, 0))

        self.pressed_key = None

        self.white_keys = [
                     Key(1 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "c", Piano.white),
                     Key(28 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "d", Piano.white),
                     Key(55 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "e", Piano.white),
                     Key(82 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "f", Piano.white),
                     Key(109 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "g", Piano.white),
                     Key(136 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "a", Piano.white),
                     Key(163 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "b", Piano.white),
                     Key(190 * self.scale_factor, 1 * self.scale_factor, 26 * self.scale_factor, 126 * self.scale_factor, "c", Piano.white)]

        self.black_keys = [Key(19 * self.scale_factor, 0, 18 * self.scale_factor, 78 * self.scale_factor, "c#", Piano.black),
                           Key(46 * self.scale_factor, 0, 18 * self.scale_factor, 78 * self.scale_factor, "d#", Piano.black),
                           Key(100 * self.scale_factor, 0, 18 * self.scale_factor, 78 * self.scale_factor, "f#", Piano.black),
                           Key(127 * self.scale_factor, 0, 18 * self.scale_factor, 78 * self.scale_factor, "g#", Piano.black),
                           Key(154 * self.scale_factor, 0, 18 * self.scale_factor, 78 * self.scale_factor, "a#", Piano.black),
                           Key(208 * self.scale_factor, 0, 9 * self.scale_factor, 78 * self.scale_factor, "c", Piano.black)]

    def is_clicked(self, mouse_x, mouse_y) -> bool:
        for key in self.black_keys:
            if key.is_valid() and key.is_pressed(mouse_x - self.x_pos, mouse_y - self.y_pos):
                key.update_color(Piano.pressed_color)
                self.pressed_key = key
                return True

        for key in self.white_keys:
            if key.is_valid() and key.is_pressed(mouse_x - self.x_pos, mouse_y - self.y_pos):
                key.update_color(Piano.pressed_color)
                self.pressed_key = key
                return True
        return False

    def get_played_note(self, octave):
        return Note(self.mixer, self.pressed_key.symbol, octave)

    def draw(self, screen):
        for key in self.white_keys:
            key.draw(self.surface)
        for key in self.black_keys:
            key.draw(self.surface)
        screen.blit(self.surface, (self.x_pos, self.y_pos))

    def reset_color(self):
        for key in self.white_keys:
            key.update_color(Piano.white)
        for key in self.black_keys:
            key.update_color(Piano.black)

    def return_note(self) -> Note:
        return None
