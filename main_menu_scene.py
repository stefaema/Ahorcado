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
        self.background = self.build_background()
        
        self.text_plot = self.build_game_plot_image()

        self.play_button = self.build_play_button()

        self.ready_for_next_scene = False

        self.sound_mixer = sound_mixer
        self.sound_mixer.play("A King's Invitation")
        
    def build_background(self):
        background = pygame.image.load('Images/Backgrounds/hangman-empty-background.png')
        scaled_background = pygame.transform.scale(background, (self.screen.get_width(), background.get_height() * self.screen.get_width() // background.get_width()))
        return scaled_background
    
    def return_next_scene(self):
        return WordPickScene(self.screen, self.sound_mixer)

    def build_game_plot_image(self):
        text= "   ¡Oíd todos, habitantes del reino! \n\n  ¡Tenemos culpable! \n ¡HANGO es el hijo d... rufián!\n Ojalá no sepa la palabra secreta... \n Todos invitados a su ejecución. \n ¡Los esperamos! :) \n                  Atte, el Rey"
        container_image = pygame.image.load('Images/Props/manuscrito.png')
        scaled_container_image = pygame.transform.scale(container_image, (2*self.screen.get_width() // 3,3* self.screen.get_height() // 4))
        font = ["fonts/PixeloidSansBold.ttf",28,(0,0,0)]
        image_x = self.screen.get_width() // 2
        image_y = self.screen.get_height() // 2
        drawable_text_image = TextToImageTool(image_x,image_y, text, *font, scaled_container_image)
        return drawable_text_image

    def build_play_button(self):
        play_button_images = ['Images/Props/play_idle.png', 'Images/Props/play_hover.png', 'Images/Props/play_pressed.png']
        play_button_images = [pygame.image.load(image) for image in play_button_images]
        play_button = Button(self.screen.get_width() - 150, self.screen.get_height() - 150, *play_button_images, 0.6)
        return play_button
    
    def update(self):
        if self.ready_for_next_scene:
            self.sound_mixer.fade_out("A King's Invitation",250)
            return self.return_next_scene()
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))
    def draw(self):
        self.draw_background()
        self.text_plot.draw(self.screen)
        self.ready_for_next_scene=self.play_button.draw(self.screen)
        if self.ready_for_next_scene:
            self.sound_mixer.play("Button Click")
        