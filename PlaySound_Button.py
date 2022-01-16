import pygame
import random
from Note import Note

class playSound_Button:
    width = 25
    height = 25

    def __init__(self, mixer, x=725, y=0) -> None:
        self.mixer = mixer
        self.image_path = "Resources/play_sound_button.png"
        self.x_pos = x
        self.y_pos = y

        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (playSound_Button.width, playSound_Button.height))

        self.collision_box = pygame.Rect(self.x_pos, self.y_pos, playSound_Button.width, playSound_Button.height)

    def is_pressed(self, event) -> bool:
        if self.collision_box.collidepoint(event.pos):
            return True
        return False

    def play_sound(self) -> Note:
        note = self.choose_note()
        note.print_note()

    def choose_note(self) -> Note:
        note_symbol = random.randint(0, len(Note.note_symbol_list) - 1)
        symbol = Note.note_symbol_list[note_symbol]

        octave_range = Note.get_octave_range(symbol)
        octave = random.randint(octave_range[0], octave_range[1])

        note = Note(self.mixer, symbol, octave)
        return note

    def draw(self, screen) -> None:
        screen.blit(self._image, (self.x_pos, self.y_pos))
