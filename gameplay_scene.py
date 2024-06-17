import pygame
from scene import Scene
from character import Character
from on_screen_keyboard import KeyboardOnScreen
from endgame_scene import EndGameScene
class GameplayScene(Scene):
    def __init__(self, screen, secret_word, sound_mixer):
        super().__init__(screen)
        self.sound_mixer = sound_mixer

        self.secret_word = secret_word

        self.background = pygame.image.load('Images/Backgrounds/hangman-structured-background.png')
        self.background = pygame.transform.scale(self.background, (screen.get_width(), self.background.get_height() * screen.get_width() // self.background.get_width()))

        self.font_path = "fonts/PixeloidSansBold.ttf"
        self.image_background = pygame.image.load('Images/Props/xd.png')
        self.keyboard = KeyboardOnScreen(screen, self.font_path, self.image_background, self.secret_word)
        self.character = Character(screen)
        self.current_word = "[]"*len(secret_word)

        self.sound_mixer.play("Dying Adventure")
    def handle_event(self, events):
        pass
    def update(self):
        self.character.update(self.keyboard.handle_mistakes())
        self.current_word = self.keyboard.get_current_word()
        if self.keyboard.did_win():
            self.sound_mixer.fade_out("Dying Adventure", 250)
            return EndGameScene(self.sound_mixer, self.screen, self.character, True)
        if self.character.did_lose():
            self.sound_mixer.fade_out("Dying Adventure", 250)
            return EndGameScene(self.sound_mixer, self.screen, self.character, False)
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        smth_incorrect_happnd, smth_correct_happnd = self.keyboard.draw()
        if smth_incorrect_happnd or smth_correct_happnd:
            self.sound_mixer.play("Button Click")
        if smth_incorrect_happnd:
            self.sound_mixer.play("Ouch Sound")
        if smth_correct_happnd:
            self.sound_mixer.play("Good Choice!")
        
        self.character.draw()
        rendered_actual_word = pygame.font.Font(self.font_path, 48).render("".join(self.current_word), True, (0, 0, 0))
        blit_x = (self.screen.get_width() - rendered_actual_word.get_width()) // 2
        blit_y = 180 - rendered_actual_word.get_height()//2
        self.screen.blit(pygame.font.Font(self.font_path, 48).render(self.current_word, True, (0, 0, 0)),(blit_x, blit_y))
