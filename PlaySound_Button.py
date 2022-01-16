import pygame
import random


class playSound_Button:
    width = 25
    height = 25

    def __init__(self, x=725, y=0) -> None:
        self.image_path = "Resources/play_sound_button.png"
        self.x_pos = x
        self.y_pos = y

        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (playSound_Button.width, playSound_Button.height))

        self.collision_box = pygame.Rect(self.x_pos, self.y_pos, playSound_Button.width, playSound_Button.height)

    def is_pressed(self, mouse_x_pos, mouse_y_pos) -> bool:
        if self.x_pos <= mouse_x_pos <= self.x_pos + playSound_Button.width:
            if self.y_pos <= mouse_y_pos <= self.y_pos + playSound_Button.height:
                return True
        return False

    def draw(self, screen) -> None:
        screen.blit(self._image, (self.x_pos, self.y_pos))
