import pygame
from scene import Scene
from button import Button
class   EndGameScene:
    def __init__(self,sound_mixer,screen,character,did_win,secret_word):
        self.character = character
        self.sound_mixer = sound_mixer
        self.did_win = did_win
        self.font_path = "fonts/PixeloidSansBold.ttf"
        self.screen = screen

        self.background = pygame.image.load('Images/Backgrounds/hangman-structured-background.png')
        self.background = pygame.transform.scale(self.background, (screen.get_width(), self.background.get_height() * screen.get_width() // self.background.get_width()))

        self.text = "¡Ganaste!" if self.did_win else "¡Perdiste!"
        self.text_surface = pygame.font.Font(self.font_path, 48).render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 8))

        self.text_word = f"La palabra era {secret_word}"
        self.text_word_surface = pygame.font.Font(self.font_path, 48).render(self.text_word, True, (0, 0, 0))
        self.text_word_rect = self.text_word_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))


        self.re_play_button_images = ['Images/Props/replay_idle.png', 'Images/Props/replay_hover.png', 'Images/Props/replay_pressed.png']
        self.re_play_button_images = [pygame.image.load(image) for image in self.re_play_button_images]
        self.re_play_button = Button(1*screen.get_width() // 4, 6*screen.get_height() // 7, *self.re_play_button_images, 0.6)

        self.ready_for_next_scene = False
        
        self.sound_mixer.play("Hango's Salvation") if self.did_win else self.sound_mixer.play("Hango's Demise")
    def handle_event(self, events):
        pass
    def update(self):
        if self.ready_for_next_scene:

            return self.new_round()
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.text_word_surface, self.text_word_rect)
        self.character.draw()

        if self.re_play_button.draw(self.screen):
            self.sound_mixer.play("Button Click")
            self.ready_for_next_scene = True
        pygame.display.flip()
        return False
    def new_round(self):
        self.sound_mixer.stop("Hango's Salvation") if self.did_win else self.sound_mixer.stop("Hango's Demise")
        from word_pick_scene import WordPickScene
        return WordPickScene(self.screen, self.sound_mixer)
