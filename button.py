import pygame
class ButtonState:
    def draw(self, button):
        pass

class IdleState(ButtonState):
    def draw(self, button):
        button.image = button.idle_image

class HoverState(ButtonState):
    def draw(self, button):
        button.image = button.hover_image

class PressedState(ButtonState):
    def draw(self, button):
        button.image = button.pressed_image
        button.clicked = True




class Button():
    def __init__(self, x, y, idle_image, hover_image, pressed_image, scale):
        self.state = IdleState()
        self.idle_image = idle_image
        self.clicked = False
        self.hover_image = hover_image
        self.pressed_image = pressed_image
        self.rect = self.idle_image.get_rect(center = (x,y))
        self.image = self.idle_image
        self.preProcessImages(scale,x,y)
         
        

    def preProcessImages(self, scale,x,y):
        width = idle_image.get_width()
        height = idle_image.get_height()
        idle_image = pygame.transform.scale(idle_image, (int(width * scale), int(height * scale)))
        hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale)))
        pressed_image = pygame.transform.scale(pressed_image, (int(width * scale), int(height * scale)))
        idle_image.set_colorkey((0,0,0))
        hover_image.set_colorkey((0,0,0))
        pressed_image.set_colorkey((0,0,0))
        rect = self.image.get_rect(center = (x,y))

    def draw(self, surface):
        action = False
        if self.isMouseOver():
            if self.isMousePressed() and not self.clicked:
                self.state = PressedState()
                action = True
            else:
                self.state = HoverState()
        else:
            self.state = IdleState()

        if not self.isMousePressed():
            self.clicked = False

        self.state.draw(self)
        surface.blit(self.image, self.rect)
        return action
    
    def isMouseOver(self):
        isMouseOver = self.rect.collidepoint(pygame.mouse.get_pos())
        return isMouseOver
    def isMousePressed(self):
        isMousePressed = pygame.mouse.get_pressed()[0] == 1
        return isMousePressed
