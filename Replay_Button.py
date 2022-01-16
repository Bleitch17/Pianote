import pygame

class replayButton:

    width = 75
    height = 75

    def __init__(self, x=30, y=30):

        self.image_path = 'Resources/replay_button.png'
        self.x_pos = x
        self.y_pos = y

        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (replayButton.width, replayButton.height))

    def draw(self, screen):
        screen.blit(self._image, (self.x_pos, self.y_pos))
        
