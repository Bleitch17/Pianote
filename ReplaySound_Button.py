import pygame

class replaySound_Button:

    width = 50
    height = 50

    def __init__(self, x=725, y=30):

        self.image_path = 'Resources/replay_button.png'
        self.x_pos = x
        self.y_pos = y

        self._image = pygame.image.load(self.image_path)
        self._image = pygame.transform.scale(self._image, (replaySound_Button.width, replaySound_Button.height))
        self.collision_box = pygame.Rect(self.x_pos, self.y_pos, replaySound_Button.width, replaySound_Button.height)

        self.playing_note = None

    def draw(self, screen):
        screen.blit(self._image, (self.x_pos, self.y_pos))
        name = pygame.font.SysFont('Roboto', 30).render("Replay Note", True, (0,0,0))
        screen.blit(name, name.get_rect(center = (self.x_pos+25, self.y_pos+70)))

    def is_pressed(self, event) -> bool:
        if self.collision_box.collidepoint(event.pos):
            return True
        return False

    def play_sound(self, expected_note):
        self.playing_note = expected_note
        if (self.playing_note != None):
            self.playing_note.print_note()
            self.playing_note.play()

            # TODO: This while loop is problematic, find a way to move it outside
            while self.playing_note.playing():
                if not self.playing_note.playing():
                    break
        
        
