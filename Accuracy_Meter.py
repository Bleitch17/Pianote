import pygame


class Accuracy_Meter:
    def __init__(self, meter_x, meter_y, needle_x, needle_y):
        self.meter_x_pos = meter_x
        self.meter_y_pos = meter_y
        self.needle_x_pos = needle_x
        self.needle_y_pos = needle_y

        self.angle = 0
        self.delta = 1

        self.meter_trans = (150, 150)
        self.needle_trans = (83, 83)

        self.meter_path = "Resources/scale.png"
        self.needle_path = "Resources/needle.png"

        self.meter = pygame.image.load(self.meter_path)
        self.meter = pygame.transform.scale(self.meter, self.meter_trans)

        self.needle = pygame.image.load(self.needle_path)
        self.needle = pygame.transform.scale(self.needle, self.needle_trans)

    def draw(self, screen):
        screen.blit(self.meter, (self.meter_x_pos, self.meter_y_pos))
        screen.blit(self.needle, (self.needle_x_pos, self.needle_y_pos))

    def adjust_angle(self, distance):
        target_angle = distance * -30

        if self.angle > target_angle:
            self.angle -= self.delta
        elif self.angle < target_angle:
            self.angle += self.delta
        self.rotate()

    def rotate(self):
        self.needle = pygame.image.load("Resources/needle.png")
        self.needle = pygame.transform.scale(self.needle, self.needle_trans)
        original_rect = self.needle.get_rect()
        needle = pygame.transform.rotate(self.needle, self.angle)
        rotated_rect = original_rect.copy()
        rotated_rect.center = needle.get_rect().center
        self.needle = needle.subsurface(rotated_rect).copy()
