import pygame, sys, math
from pygame.locals import *


class Game:
    def __init__(self, screen, width, height, clock):

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)


        self.running = False

    def run(self):

        # main loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            left, middle, right = pygame.mouse.get_pressed()
            mouseX, mouseY = pygame.mouse.get_pos()


            self.screen.fill(self.white)

            pygame.draw.line(self.screen, self.black, (0,0), (pygame.mouse.get_pos()))

            


            pygame.display.update()
            self.clock.tick(60)