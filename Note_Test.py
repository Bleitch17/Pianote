import pygame
from Note import Note


if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.set_num_channels(12)

    note = Note(pygame.mixer)
    note.play()

    while note.playing():
        if not note.playing():
            break
