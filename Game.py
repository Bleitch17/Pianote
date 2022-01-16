import pygame, sys, math
from PlaySound_Button import playSound_Button
from ReplaySound_Button import replaySound_Button
from pygame.locals import *


class Game:
    def __init__(self, screen, width, height, clock):

        pygame.mixer.init()
        pygame.mixer.set_num_channels(12)

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock

        # Create a playSound button:
        self.play_sound_button = playSound_Button(pygame.mixer, x=self.width-75, y=0)

        # Create a replay button:
        self.replay_sound_button = replaySound_Button()

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (50.2, 50.2, 50.2)

        self.running = True

    def run(self):

        # main loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    left, middle, right = pygame.mouse.get_pressed()
                    mouseX, mouseY = pygame.mouse.get_pos()

                    # Call the collision checking functions of the various objects:
                    if self.play_sound_button.is_pressed(event):
                        self.play_sound_button.play_sound()
                    elif self.replay_sound_button.is_pressed(event):
                        self.replay_sound_button.play_sound()
                    

            self.screen.fill(self.white)

            left, middle, right = pygame.mouse.get_pressed()
            mouseX, mouseY = pygame.mouse.get_pos()

            #137 pixels wide
            #639 pixels tall

            #40 pixels left
            #45 pixels right
            #390 pixels tall

            # 5 pixels wide


            # piano = pygame.image.load('Resources/Piano_Keyboard.png')
            # piano.convert()
            # piano = pygame.transform.rotozoom(piano, 0, 0.3)
            # pianoRect = piano.get_rect()
            # pianoRect.center = self.width//2, self.height//2

            # self.screen.blit(piano, pianoRect)

            pianoPos = (self.width//2 - 110, 3*self.height//5)
            pianoSurface = pygame.Surface((217, 128))
            pianoSurface.fill((0, 0, 0))
            key1 = pygame.Rect(1,1,26,126)
            key3 = pygame.Rect(28,1,26,126)
            key5 = pygame.Rect(55,1,26,126)
            key6 = pygame.Rect(82,1,26,126)
            key8 = pygame.Rect(109,1,26,126)
            key10 = pygame.Rect(136,1,26,126)
            key12 = pygame.Rect(163,1,26,126)
            key13 = pygame.Rect(190,1,26,126)

            key2 = pygame.Rect(19,0,18,78)
            key4 = pygame.Rect(46,0,18,78)
            key7 = pygame.Rect(100,0,18,78)
            key9 = pygame.Rect(127,0,18,78)
            key11 = pygame.Rect(154,0,18,78)
            key14 = pygame.Rect(208,0,9,78)


            key1c, key3c, key5c, key6c, key8c, key10c, key12c, key13c, key2c, key4c, key7c, key9c, key11c, key14c = self.white, self.white, self.white, self.white, self.white, self.white, self.white, self.white, self.black, self.black, self.black, self.black, self.black, self.black
            keyPressedColor = (150, 150, 150)

            if left:
                if key2.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key2c = keyPressedColor
                    print("key2")
                elif key4.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key4c = keyPressedColor
                    print("key4")
                elif key7.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key7c = keyPressedColor
                    print("key7")
                elif key9.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key9c = keyPressedColor
                    print("key9")
                elif key11.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key11c = keyPressedColor
                    print("key11")
                elif key14.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key14c = keyPressedColor
                    print("key14")
                elif key1.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key1c = keyPressedColor
                    print("key1")
                elif key3.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key3c = keyPressedColor
                    print("key3")
                elif key5.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key5c = keyPressedColor
                    print("key5")
                elif key6.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key6c = keyPressedColor
                    print("key6")
                elif key8.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key8c = keyPressedColor
                    print("key8")
                elif key10.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key10c = keyPressedColor
                    print("key10")
                elif key12.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key12c = keyPressedColor
                    print("key12")
                elif key13.collidepoint(mouseX-pianoPos[0], mouseY-pianoPos[1]):
                    key13c = keyPressedColor
                    print("key13")


            
            
            pygame.draw.rect(pianoSurface, key1c, key1)            
            pygame.draw.rect(pianoSurface, key3c, key3)
            pygame.draw.rect(pianoSurface, key5c, key5)
            pygame.draw.rect(pianoSurface, key6c, key6)
            pygame.draw.rect(pianoSurface, key8c, key8)
            pygame.draw.rect(pianoSurface, key10c, key10)
            pygame.draw.rect(pianoSurface, key12c, key12)
            pygame.draw.rect(pianoSurface, key13c, key13)
            pygame.draw.rect(pianoSurface, key2c, key2)
            pygame.draw.rect(pianoSurface, key4c, key4)
            pygame.draw.rect(pianoSurface, key7c, key7)
            pygame.draw.rect(pianoSurface, key9c, key9)
            pygame.draw.rect(pianoSurface, key11c, key11)
            pygame.draw.rect(pianoSurface, key14c, key14)
            self.screen.blit(pianoSurface, pianoPos)

            # Draw the replay button
            self.replay_sound_button.draw(self.screen)
            
            # Draw the playSound button
            self.play_sound_button.draw(self.screen)
            

            pygame.draw.line(self.screen, self.black, (0,0), (pygame.mouse.get_pos()))

            #accuracy meter
            meter = pygame.image.load("Resources/scale.png")
            meter = pygame.transform.scale(meter, (150, 150))
            self.screen.blit(meter, (self.width//2 - 75, self.height//4.5))

            needle = pygame.image.load("Resources/needle.png")
            needle = pygame.transform.scale(needle, (150, 150))
            self.screen.blit(needle, (self.width//2 - 75, self.height//4.5))
            

            pygame.display.update()
            self.clock.tick(60)