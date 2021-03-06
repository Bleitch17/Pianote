import pygame, sys, math
from PlaySound_Button import playSound_Button
from ReplaySound_Button import replaySound_Button
from Piano import Piano
from Accuracy_Meter import Accuracy_Meter
from Button import Button
from Note import Note
from pygame.locals import *
import globalvars
from Star import Star

class Game:
    def __init__(self, screen, width, height, clock):

        pygame.mixer.init()
        pygame.mixer.set_num_channels(12)

        self.screen = screen
        self.width = width
        self.height = height
        self.clock = clock
        
        # Create Star
        self.star = Star()

        # Create the button to the menu
        self.menubutton = Button(150, 100, 200, 100, "Main Menu", (156, 219, 177), (0, 0, 0), 40)

        # Create a playSound button:
        self.play_sound_button = playSound_Button(pygame.mixer, 3*self.width/4-100, 50)

        # Create a replay button:
        self.replay_sound_button = replaySound_Button(3*self.width/4+50, 50)

        # Create a piano:
        self.piano = Piano(pygame.mixer, (self.width - 217 * 2)//2, 450, 2)

        # Create meter
        self.meter = Accuracy_Meter(self.width // 2 - 75, self.height // 4.5, self.width // 2 - 42,
                                    self.height // 4 + 28, self.width, self.height)

        # Keep track of the "correct"  and "actual" note
        self.expected_note = None
        self.actual_note = None

        # Determines whether the piano has been played
        self.piano_played = False

        # distance between expected and actual:
        self.distance = 0

        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (50.2, 50.2, 50.2)

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
                    self.piano_played = False
                    left, right, middle = pygame.mouse.get_pressed()
                    if self.play_sound_button.is_pressed(event) and left:
                        self.play_sound_button.play_sound()
                        self.expected_note = self.play_sound_button.get_playing_note()

                    elif self.replay_sound_button.is_pressed(event) and left:
                        print(self.expected_note)
                        self.replay_sound_button.play_sound(self.expected_note)

                    if self.piano.is_clicked(mouseX, mouseY) and self.expected_note is not None:
                        self.piano_played = True
                        self.actual_note = self.piano.get_played_note(self.expected_note.get_octave())
                        self.actual_note.print_note()
                        self.actual_note.play()

                        difference = Note.distance(self.actual_note, self.expected_note)
                        if  difference == 0:
                            self.star.incr_decr_Star(True)
                        else: 
                            self.star.incr_decr_Star(False)

                    if self.menubutton.is_pressed(event) and left:
                        print("Hello")
                        globalvars.currentScene = "menu"
                        print(globalvars.currentScene)
                        self.running = False
                        break

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.piano.reset_color()
                    if self.expected_note is not None and self.actual_note is not None and self.piano_played:
                        self.distance = Note.distance(self.expected_note, self.actual_note)

            self.screen.fill((194, 225, 231))

            # Draw Star
            self.star.updateStars()
            self.star.drawStars(self.screen)

            # Draw the replay button
            self.replay_sound_button.draw(self.screen)
            
            # Draw the playSound button
            self.play_sound_button.draw(self.screen)

            # Draw the piano
            self.piano.draw(self.screen)

            # Meter
            self.meter.adjust_angle(self.distance)
            self.meter.draw(self.screen)

            # Draw the menu button
            self.menubutton.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)