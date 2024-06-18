import pygame
from scene import Scene
from animations import Animation, LinearStraightMovementStrategy
from sprite_sheet import SpriteSheet
from main_menu_scene import MainMenuScene
import time

class LoadingScene(Scene):
    def __init__(self, screen,sound_mixer, clock,loading_time=2):
        super().__init__(screen)
        self.clock = clock
        self.loading_time = loading_time
        FRAME_PER_SECOND = 24
        self.font = pygame.font.Font("fonts/PixeloidSansBold.ttf", 64)
        self.text = "Ahorcado"
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))
        initial_pos = ((self.screen.get_width() -1)//4, (self.screen.get_height() -1)//2)
        final_pos = ((self.screen.get_width() -1)*3//4, (self.screen.get_height() -1)//2)
        delay_per_frame = loading_time * FRAME_PER_SECOND // 8
        self.animation = Animation(self.screen, delay_per_frame , SpriteSheet("320x320","Images/HangManWalking/HangManWalking.png"),LinearStraightMovementStrategy(initial_pos, final_pos, loading_time), scale=0.8)
        self.initial_time = time.time()
        self.sound_mixer = sound_mixer
        self.sound_mixer.play("Stepping On Grass")

    def handle_event(self, events):
        pass
    def update(self):
        if time.time() - self.initial_time > self.loading_time:
            self.sound_mixer.stop("Stepping On Grass")
            return MainMenuScene(self.screen, self.sound_mixer)
            

        self.animation.update()

    def draw(self):
        self.screen.fill((204, 236, 239))
        self.screen.blit(self.text_surface, self.text_rect)
        self.animation.draw()