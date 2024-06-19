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
        SCR_WIDTH = screen.get_width()
        SCR_HEIGHT = screen.get_height()
        self.sound_mixer = sound_mixer
        self.sound_mixer.play("Executioner's Remorse")


        self.text_surface, self.text_rect = self.build_subtitle(SCR_WIDTH, SCR_HEIGHT)

        self.warning_surface, self.warning_rect, self.warning_text, self.font_warning = self.build_warning_text(SCR_WIDTH, SCR_HEIGHT)

        self.input_box = self.build_input_box(SCR_WIDTH, SCR_HEIGHT)

        self.lever = self.build_secure_input_toggle(SCR_WIDTH, SCR_HEIGHT)

        self.executioner_animation = self.build_executioner_animation(SCR_WIDTH, SCR_HEIGHT)

        self.play_button = self.build_play_button(SCR_WIDTH, SCR_HEIGHT)

        self.ready_for_next_scene = False

        self.secret_word = ""   

    def build_warning_text(self, SCR_WIDTH, SCR_HEIGHT):
        font_warning = pygame.font.Font("fonts/PixeloidSansBold.ttf", 32)
        text = ""
        text_surface = font_warning.render(text, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(SCR_WIDTH // 2, SCR_HEIGHT // 4))
        return text_surface, text_rect ,text, font_warning

    def build_subtitle(self, SCR_WIDTH, SCR_HEIGHT):
        font_subtitle = pygame.font.Font("fonts/PixeloidSansBold.ttf", 48)
        text = "Ingresa la palabra de salvación"
        text_surface = font_subtitle.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(SCR_WIDTH // 2, SCR_HEIGHT // 8))
        return text_surface, text_rect
    def build_play_button(self, SCR_WIDTH, SCR_HEIGHT):
        play_button_images = ['Images/Props/play_idle.png', 'Images/Props/play_hover.png', 'Images/Props/play_pressed.png']
        play_button_images = [pygame.image.load(image) for image in play_button_images]
        play_button = Button(SCR_WIDTH // 2 + 300, SCR_HEIGHT // 2 + 50, *play_button_images, 0.4)
        return play_button

    def build_executioner_animation(self, SCR_WIDTH, SCR_HEIGHT):
        executioner_sprite_sheet = SpriteSheet("320x320", "Images/Executioner/Executioner.png")
        initial_pos = ((SCR_WIDTH - 1) // 3 + 100, (SCR_HEIGHT - 1) * 2 // 3)
        final_pos = ((SCR_WIDTH - 1) * 3 // 3 + 100, (SCR_HEIGHT - 1) // 2)
        executioner_animation = Animation(self.screen, 20, executioner_sprite_sheet, NoMovementStrategy(initial_pos), 0.7)
        return executioner_animation


    def build_secure_input_toggle(self, SCR_WIDTH, SCR_HEIGHT):
        toggle_images = ['Images/Props/pass_on.png', 'Images/Props/pass_off.png', 'Images/Props/pass_on_off.png', 'Images/Props/pass_off_on.png']
        toggle_images = [pygame.image.load(image) for image in toggle_images]
        toggle_position = (SCR_WIDTH//3 + 90, SCR_HEIGHT // 2 - 50)
        toggle = Lever(*toggle_position, *toggle_images, 0.35)
        return toggle

    def build_input_box(self, SCR_WIDTH, SCR_HEIGHT):
        image = pygame.image.load('Images/Props/thinkin.png')
        image = pygame.transform.scale(image, (int(image.get_width() * 0.6) + 100, int(image.get_height() * 0.6)))
        input_box_position = (SCR_WIDTH // 2 + 150, SCR_HEIGHT // 2)
        input_box = InputBox(image, input_box_position)
        return input_box
    def handle_event(self, events):
        for event in events:
            self.input_box.handle_event(event)

    def update(self):
        self.input_box.update()
        self.executioner_animation.update()
        self.warning_surface = self.font_warning.render(self.warning_text, True, (255, 0, 0))
        if self.ready_for_next_scene:
            self.sound_mixer.fade_out("Executioner's Remorse",250)
            return self.return_next_scene()

    def return_next_scene(self):
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

            
        