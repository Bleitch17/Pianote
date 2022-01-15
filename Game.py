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

        self.running = True

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

            piano = pygame.image.load('Resources/Piano_Keyboard.png')
            piano.convert()
            pianoRect = piano.get_rect()
            pianoRect.center = self.width//2, self.height//2

            self.screen.blit(piano, pianoRect)


            pygame.draw.rect(self.screen, self.black, pygame.Rect(30,30,60,60))
            replay = pygame.image.load('Resources/replay_button.png')
            replay.convert()
            replayRect = replay.get_rect()
            #replayRect.inflate(-100, -100)
            replayRect.fit(pygame.Rect(30,30,60,60))
            #replayRect.center = self.width//2, self.height//2

            self.screen.blit(replay, replayRect)

            pygame.draw.line(self.screen, self.black, (0,0), (pygame.mouse.get_pos()))

            

            print("Running Game")
            pygame.display.update()
            self.clock.tick(60)