import pygame, sys, math
from Piano import Piano
from Button import Button
from pygame.locals import *
import globalvars

class Star:
    #global counter to keep track of number of correct answer
    #print a star with number of correct answers
    positions = [(0,0), (0, 50), (0, 100), (0,150), (0, 200)]
    star1 = 5
    star2 = 10
    star3 = 15
    star4 = 20
    star5 = 30
    width = 30
    height = 30

    def __init__(self):
        self.count = 0
        self.stars = 0
        self.image_path = "Resources/star.png"
        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (Star.width, Star.height))
    
    def incr_decr_Star(self, bool):

        if bool == True:
            self.count += 1
        else:
            if self.count != 0:
                self.count -= 1
    
    #get correct number of stars
    def updateStars(self) -> None:
        
        if self.count >= 0 and self.count < Star.star1:
            self.stars = 0
        elif self.count >= Star.star1 and self.count < Star.star2:
            self.stars = 1
        elif self.count >= Star.star2 and self.count < Star.star3:
            self.stars = 2
        elif self.count >= Star.star3 and self.count < Star.star4:
            self.stars = 3
        elif self.count >= Star.star4 and self.count < Star.star5:
            self.stars = 4
        else:
            self.stars = 5      

    def drawStars(self, screen):
        
        for i in range(0,self.stars):
            screen.blit(self._image, Star.positions[i])

            

        
