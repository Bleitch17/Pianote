import pygame
import random

class Button:

    def __init__(self, x, y, w, h, text, color, fontColor, fontSize) -> None:
        self.x_pos = x
        self.y_pos = y
        self.width = w
        self.height = h
        self.text = text
        self.color = color
        self.fontColor = fontColor
        self.fontSize = fontSize
        self.font = pygame.font.SysFont('Roboto', fontSize)

        self.collision_box = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.collision_box.center = (self.x_pos, self.y_pos)

        self.playing_note = None

    def is_pressed(self, event) -> bool:
        if self.collision_box.collidepoint(event.pos):
            return True
        return False

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.collision_box)
        drawtext = self.font.render(self.text, True, self.fontColor)
        screen.blit(drawtext, drawtext.get_rect(center = (self.x_pos, self.y_pos)))
        
