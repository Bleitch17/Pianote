import pygame


class Note:
    def __init__(self, mixer, symbol='c', octave=4):
        self.mixer = mixer
        self.symbol = symbol
        self.octave = octave

        self.name = symbol + str(octave)
