import pygame
from scenes import *
from animations import *


def screenGen():
    info = pygame.display.Info()
    SCREEN_WIDTH = (3*info.current_w)/4
    SCREEN_HEIGHT = (3*info.current_h)/4
    screen = pygame.display.set_mode((int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
    pygame.display.set_caption('Ahorcado')
    pygame.display.set_icon(pygame.image.load('Images/Favicon/favicon.png'))
    return screen



# Inicializar Pygame
pygame.init()

screen = screenGen()

clock = pygame.time.Clock()

current_scene = LoadingScene(screen,2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Manejar eventos y actualizar la escena actual
    current_scene.handle_events(pygame.event.get())
    next_scene = current_scene.update()
    if next_scene is not None:
        current_scene = next_scene

    # Dibujar la escena actual
    current_scene.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()