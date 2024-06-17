import pygame
from animations import Animation, NoMovementStrategy
from sprite_sheet import SpriteSheet
from input_box import InputBox
from lever import Lever
from scene import Scene
from button import Button


from gameplay_scene import GameplayScene
class WordPickScene(Scene):
    def __init__(self,screen, sound_mixer):
        super().__init__(screen)
        self.sound_mixer = sound_mixer
        self.sound_mixer.play("Executioner's Remorse")

        self.font_subtitle = pygame.font.Font("fonts/PixeloidSansBold.ttf", 48)
        self.text = "Ingresa la palabra de salvación"
        self.text_surface = self.font_subtitle.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 8))

        self.font_warning = pygame.font.Font("fonts/PixeloidSansBold.ttf", 32)
        self.warning_text = ""
        self.warning_surface = self.font_warning.render(self.warning_text, True, (255, 0, 0))
        self.warning_rect = self.warning_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))

        image = pygame.image.load('Images/Props/thinkin.png')
        image = pygame.transform.scale(image, (int(image.get_width() * 0.6) + 100, int(image.get_height() * 0.6)))
        self.input_box = InputBox(image, (screen.get_width() // 2 + 150, screen.get_height() // 2))

        self.lever_images = ['Images/Props/pass_on.png', 'Images/Props/pass_off.png', 'Images/Props/pass_on_off.png', 'Images/Props/pass_off_on.png']
        #self.lever_images = ['Images/Props/pass_off.png', 'Images/Props/pass_on.png', 'Images/Props/pass_off_on.png', 'Images/Props/pass_on_off.png']
        self.lever_images = [pygame.image.load(image) for image in self.lever_images]
        self.lever = Lever(screen.get_width()//3+90,2* screen.get_height() // 4 - 50, *self.lever_images, 0.35)

        self.executioner_sprite_sheet=SpriteSheet("320x320","Images/Executioner/Executioner.png")
        initial_pos = ((self.screen.get_width() -1)//3+100, (self.screen.get_height() -1)*2//3)
        final_pos = ((self.screen.get_width() -1)*3//3 +100, (self.screen.get_height() -1)//2)
        self.executioner_animation = Animation(screen, 20, self.executioner_sprite_sheet, initial_pos, final_pos, 1, NoMovementStrategy(), 0.7)

        play_button_images = ['Images/Props/play_idle.png', 'Images/Props/play_hover.png', 'Images/Props/play_pressed.png']
        play_button_images = [pygame.image.load(image) for image in play_button_images]
        self.play_button = Button(screen.get_width() // 2 + 300, screen.get_height() // 2 + 50, *play_button_images, 0.4)

        self.ready_for_next_scene = False
        self.secret_word = ""   

    def handle_event(self, events):
        for event in events:
            self.input_box.handle_event(event)

    def update(self):
        self.input_box.update()
        self.executioner_animation.update()
        if self.ready_for_next_scene:
            self.sound_mixer.fade_out("Executioner's Remorse",250)
            return GameplayScene(self.screen, self.secret_word, self.sound_mixer)

    def bad_input(self):
        self.warning_text = self.input_box.verification_strategy.criteria()
        print(self.warning_text)
        self.input_box.empty()
    def draw(self):
        self.screen.fill((204, 236, 239))
        self.screen.blit(self.text_surface, self.text_rect)
        self.input_box.draw(self.screen)
        self.input_box.set_secure_text_entry(not self.lever.toggled())
        

        self.warning_surface = self.font_warning.render(self.warning_text, True, (255, 0, 0))
        self.warning_rect = self.warning_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 4- 50) )
        self.screen.blit(self.warning_surface, self.warning_rect)
        self.lever.draw(self.screen)
        self.executioner_animation.draw()
        submit = self.play_button.draw(self.screen)

        if submit:
            self.sound_mixer.play("Button Click")
            if self.input_box.verify():
                self.ready_for_next_scene = True  
                self.secret_word = self.input_box.get_text()
            else:
                self.bad_input()

            
        