import pygame
import random


class playSound_Button:
    width = 25
    height = 25

    def __init__(self, x=725, y=0):
        self.image_path = "Resources/play_sound_button.png"
        self.x_pos = x
        self.y_pos = y

        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (playSound_Button.width, playSound_Button.height))

    def draw(self, screen):
        screen.blit(self._image, (self.x_pos, self.y_pos))
