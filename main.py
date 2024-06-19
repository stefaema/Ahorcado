import pygame
from scene import Scene
from loading_scene import LoadingScene
from word_pick_scene import WordPickScene
from main_menu_scene import MainMenuScene
from gameplay_scene import GameplayScene
from sound_mixer import SoundMixer
def screenGenerator():
    info = pygame.display.Info()
    SCREEN_WIDTH = (3*info.current_w)/4
    SCREEN_HEIGHT = (3*info.current_h)/4
    screen = pygame.display.set_mode((int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
    pygame.display.set_caption('Ahorcado')
    pygame.display.set_icon(pygame.image.load('Images/Favicon/favicon.png'))
    return screen

# Inicializar Pygame
pygame.init()

screen = screenGenerator()

clock = pygame.time.Clock()

sound_mixer =   SoundMixer()
is_game_running = True

#current_scene = LoadingScene(screen,sound_mixer, clock, 2)
current_scene = WordPickScene(screen, sound_mixer)

while is_game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

        current_scene.handle_event([event])

    next_scene = current_scene.update()

    if next_scene is not None:
        current_scene = next_scene

    current_scene.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()