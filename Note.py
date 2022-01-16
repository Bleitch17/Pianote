import pygame


class Note:
    note_symbol_list = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    octave_range1 = [0, 7]
    octave_range2 = [1, 7]
    octave_range3 = [1, 8]

    def __init__(self, mixer, symbol="c", octave=4) -> None:
        self.mixer = mixer
        self.symbol = symbol
        self.octave = octave
        self.channel_num = self.find_channel_num()

        if octave == 0:
            if self.symbol == "a" or self.symbol == "a#" or self.symbol == "b":
                self.octave = 0
            else:
                self.octave = 1

        self.name = symbol + str(self.octave)

        # Bug waiting to happen: if A0 is randomly chosen, and I play d on the keyboard, this line will crash
        # Also happens if the extra note is played
        self.sound = mixer.Sound("Audio/" + f"{self.name}" + ".wav")

    def find_channel_num(self) -> int:
        for symbol in Note.note_symbol_list:
            if symbol == self.symbol:
                return Note.note_symbol_list.index(symbol)

    def play(self, maxtime=2000, fade_ms=125) -> None:
        self.mixer.Channel(self.channel_num).play(self.sound, loops=0, maxtime=maxtime, fade_ms=fade_ms)

    def playing(self) -> bool:
        return self.mixer.Channel(self.channel_num).get_busy()

    def get_symbol(self):
        return self.symbol

    def get_octave(self):
        return self.octave

    def print_note(self) -> None:
        print(self.name)

    @staticmethod
    def get_octave_range(note_symbol):
        if note_symbol == 'a#' or note_symbol == 'a' or note_symbol == 'b':
            return Note.octave_range1
        elif note_symbol == 'c':
            return Note.octave_range3
        else:
            return Note.octave_range2
