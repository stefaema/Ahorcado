import pygame
from scene import Scene
from animations import Animation, LinearStraightMovementStrategy, NoMovementStrategy
from sprite_sheet import SpriteSheet
from main_menu_scene import MainMenuScene
import random
import time

class LoadingScene(Scene):
    def __init__(self, screen, sound_mixer, clock,loading_time=2):
        super().__init__(screen)
        SCR_WIDTH = self.screen.get_width()
        SCR_HEIGHT = self.screen.get_height()
        self.clock = clock
        self.loading_time = loading_time
        
        self.text_surface, self.text_rect = self.build_text_surface(SCR_WIDTH, SCR_HEIGHT)

        FRAME_PER_SECOND = 24
        self.delay_per_frame = loading_time * FRAME_PER_SECOND // 6

        self.animation = self.build_loading_animation(SCR_WIDTH, SCR_HEIGHT)

        self.initial_time = time.time()

        self.sound_mixer = sound_mixer

        self.reset_point_reached = False
        self.sound_mixer.play("Stepping On Grass")
    
    def get_elapsed_time(self):
        return time.time() - self.initial_time

    def return_next_scene(self):
        return MainMenuScene(self.screen, self.sound_mixer)
    
    def update(self):
        
        
        if self.get_elapsed_time() > self.loading_time//3:
            self.change_animation()

        self.animation.update()

        if self.get_elapsed_time()> self.loading_time:
            self.sound_mixer.stop("Stepping On Grass")
            return self.return_next_scene()
            

    def change_animation(self):
        self.sound_mixer.fade_out("Stepping On Grass",250)
        self.animation.sprite_sheet = SpriteSheet("320x320","Images/HangManWalking/HangManWalking2.png")
        self.animation.movement_strategy = NoMovementStrategy((self.animation.x, self.animation.y))
        if not self.reset_point_reached:
            self.reset_point_reached = True
            self.animation.reset(self.delay_per_frame, loop=False)

    def build_loading_animation(self, SCR_WIDTH, SCR_HEIGHT):
        initial_pos = ((SCR_WIDTH -1)//6, (SCR_HEIGHT -1)//2)
        final_pos = ((SCR_WIDTH -1)//2, (SCR_HEIGHT -1)//2)
        sprite_sheet = SpriteSheet("320x320","Images/HangManWalking/HangManWalking.png")
        movement_strategy = LinearStraightMovementStrategy(initial_pos, final_pos, self.loading_time//3)
        scale = 0.8
        return Animation(self.screen,self.delay_per_frame, sprite_sheet, movement_strategy, scale)

    def build_text_surface(self, SCR_WIDTH, SCR_HEIGHT):
        font = pygame.font.Font("fonts/PixeloidSansBold.ttf", 64)
        text = "Ahorcado"
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(SCR_WIDTH // 2, SCR_HEIGHT // 4))
        return text_surface, text_rect
    
    def draw(self):
        self.screen.fill((204, 236, 239))
        self.screen.blit(self.text_surface, self.text_rect)
        self.animation.draw()