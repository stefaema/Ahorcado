import pygame
from scene import Scene
from animations import Animation
from sprite_sheet import SpriteSheet
from button import Button
from word_pick_scene import WordPickScene
from text_to_image import TextToImageTool
class MainMenuScene(Scene):
    def __init__(self, screen, sound_mixer):
        super().__init__(screen)
        self.background = pygame.image.load('Images/Backgrounds/hangman-empty-background.png')
        self.background = pygame.transform.scale(self.background, (screen.get_width(), self.background.get_height() * screen.get_width() // self.background.get_width()))
        self.text_container_image = pygame.image.load('Images/Props/manuscrito.png')
        text= "   ¡Oíd todos, habitantes del reino! \n\n  ¡Tenemos culpable! \n ¡HANGO es el hijo d... rufián!\n Ojalá no sepa la palabra secreta... \n Todos invitados a su ejecución. \n ¡Los esperamos! :) \n                  Atte, el Rey"
        self.text_container_image = pygame.transform.scale(self.text_container_image, (2*screen.get_width() // 3,3* screen.get_height() // 4))
        self.text_plot = TextToImageTool(screen.get_width() // 2, screen.get_height() // 2, text, "fonts/PixeloidSansBold.ttf", 28, (0, 0, 0), background_surface=self.text_container_image)
    
        play_button_images = ['Images/Props/play_idle.png', 'Images/Props/play_hover.png', 'Images/Props/play_pressed.png']
        play_button_images = [pygame.image.load(image) for image in play_button_images]
        self.play_button = Button(screen.get_width() - 150, screen.get_height() - 150, *play_button_images, 0.6)
        self.ready_for_next_scene = False

        self.sound_mixer = sound_mixer
        self.sound_mixer.play("A King's Invitation")
    def update(self):
        if self.ready_for_next_scene:
            self.sound_mixer.fade_out("A King's Invitation",250)
            return WordPickScene(self.screen, self.sound_mixer)
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.text_plot.draw(self.screen)
        self.ready_for_next_scene=self.play_button.draw(self.screen)
        if self.ready_for_next_scene:
            self.sound_mixer.play("Button Click")
        pygame.display.flip()