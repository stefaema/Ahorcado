import pygame

class Button():
    def __init__(self, x, y, idle_image, hover_image, pressed_image, scale):
        width = idle_image.get_width()
        height = idle_image.get_height()
        self.idle_image = pygame.transform.scale(idle_image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale)))
        self.pressed_image = pygame.transform.scale(pressed_image, (int(width * scale), int(height * scale)))
        self.idle_image.set_colorkey((0,0,0))
        self.hover_image.set_colorkey((0,0,0))
        self.pressed_image.set_colorkey((0,0,0))
        self.image = self.idle_image
        self.rect = self.image.get_rect(center = (x,y))
        
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = self.hover_image
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.image = self.pressed_image
                self.clicked = True
                action = True
        else:
            self.image = self.idle_image

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, self.rect)

        return action