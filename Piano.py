import pygame
from Note import Note
from Key import Key


class Piano:
    black = (0, 0, 0)
    white = (255, 255, 255)
    pressed_color = (150, 150, 150)

    def __init__(self, mixer, x, y):
        self.mixer = mixer
        self.x_pos = x
        self.y_pos = y

        self.surface = pygame.Surface((217, 128))
        self.surface.fill((0, 0, 0))

        # Order matters!
        self.white_keys = [
                     Key(1, 1, 26, 126, "c", Piano.white),
                     Key(28, 1, 26, 126, "d", Piano.white),
                     Key(55, 1, 26, 126, "e", Piano.white),
                     Key(82, 1, 26, 126, "f", Piano.white),
                     Key(109, 1, 26, 126, "g", Piano.white),
                     Key(136, 1, 26, 126, "a", Piano.white),
                     Key(163, 1, 26, 126, "b", Piano.white),
                     Key(190, 1, 26, 126, "c", Piano.white)]

        self.black_keys = [Key(19, 0, 18, 78, "c#", Piano.black),
                           Key(46, 0, 18, 78, "d#", Piano.black),
                           Key(100, 0, 18, 78, "f#", Piano.black),
                           Key(127, 0, 18, 78, "g#", Piano.black),
                           Key(154, 0, 18, 78, "a#", Piano.black),
                           Key(208, 0, 9, 78, "extra", Piano.black)]

    def check_collision(self, mouse_x, mouse_y) -> None:
        key_pressed = False
        for key in self.black_keys:
            if key.is_pressed(mouse_x - self.x_pos, mouse_y - self.y_pos):
                key.update_color(Piano.pressed_color)
                key_pressed = True
                break
            else:
                key.update_color(Piano.black)

        if key_pressed:
            for key in self.white_keys:
                key.update_color(Piano.white)
        else:
            for key in self.white_keys:
                if key.is_pressed(mouse_x - self.x_pos, mouse_y - self.y_pos):
                    key.update_color(Piano.pressed_color)
                else:
                    key.update_color(Piano.white)


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
