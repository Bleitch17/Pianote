import pygame, sys, math
from PlaySound_Button import playSound_Button
from ReplaySound_Button import replaySound_Button
from Piano import Piano
from Button import Button
from pygame.locals import *
import globalvars


class Game:
    def __init__(self, screen, width, height, clock):

        pygame.mixer.init()
        pygame.mixer.set_num_channels(12)

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
        
        # Create the button to the menu
        self.menubutton = Button(100, 100, 100, 100, "Main Menu", (255, 255, 0), (0, 0, 0))

        # Create a playSound button:
        self.play_sound_button = playSound_Button(pygame.mixer, x=self.width-75, y=0)

        # Create a replay button:
        self.replay_sound_button = replaySound_Button()

        # Create a piano:
        self.piano = Piano(pygame.mixer, self.width//2 - 110, 3*self.height//5)

        # Keep track of the "correct"  and "actual" note
        self.expected_note = None
        self.actual_note = None

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (50.2, 50.2, 50.2)

        # angle
        self.angle = 0

        self.running = True

    def run(self):
        # main loop
        while self.running:
            mouseX, mouseY = pygame.mouse.get_pos()
            left, right, middle = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Call the collision checking functions of the various objects:
                    left, right, middle = pygame.mouse.get_pressed()
                    if self.play_sound_button.is_pressed(event) and left:
                        self.play_sound_button.play_sound()
                        self.expected_note = self.play_sound_button.get_playing_note()

                    elif self.replay_sound_button.is_pressed(event) and left:
                        print(self.expected_note)
                        self.replay_sound_button.play_sound(self.expected_note)

                    if self.piano.is_clicked(mouseX, mouseY) and self.expected_note is not None:
                        self.actual_note = self.piano.get_played_note(self.expected_note.get_octave())
                        self.actual_note.print_note()

                    if self.menubutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "menu"
                        print(globalvars.currentScene)
                        self.running = False
                        break

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.piano.reset_color()

            self.screen.fill(self.white)

            # Draw the replay button
            self.replay_sound_button.draw(self.screen)
            
            # Draw the playSound button
            self.play_sound_button.draw(self.screen)

            # Draw the piano
            self.piano.draw(self.screen)

            #accuracy meter
            meter = pygame.image.load("Resources/scale.png")
            meter = pygame.transform.scale(meter, (150, 150))
            self.screen.blit(meter, (self.width//2 - 75, self.height//4.5))

            needle = pygame.image.load("Resources/needle.png")
            needle = pygame.transform.scale(needle, (83, 83))
            original_rect = needle.get_rect()
            needle = pygame.transform.rotate(needle, self.angle)
            rotated_rect = original_rect.copy()
            rotated_rect.center = needle.get_rect().center
            needle = needle.subsurface(rotated_rect).copy()
            self.screen.blit(needle, (self.width//2-42, self.height//4+28))

            # Draw the menu button
            self.menubutton.draw(self.screen)
            

            pygame.display.update()
            self.clock.tick(60)
            self.angle-= 1