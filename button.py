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
    def validate_parameters(self, x, y, idle_image, hover_image, pressed_image, scale):
        if not isinstance(idle_image, pygame.Surface):
            raise ValueError("Idle image must be a pygame.Surface object")
        if not isinstance(hover_image, pygame.Surface):
            raise ValueError("Hover image must be a pygame.Surface object")
        if not isinstance(pressed_image, pygame.Surface):
            raise ValueError("Pressed image must be a pygame.Surface object")
        if not isinstance(scale, (int, float)):
            raise ValueError("Scale must be an integer or a float")
        if not isinstance(x, int):
            raise ValueError("x must be an integer")
        if not isinstance(y, int):
            raise ValueError("y must be an integer")
        
    def __init__(self, x, y, idle_image, hover_image, pressed_image, scale):
        self.validate_parameters(x, y, idle_image, hover_image, pressed_image, scale)
        self.state = IdleState()
        self.mouse_exited_after_click = False
        self.idle_image = idle_image
        self.hover_image = hover_image
        self.pressed_image = pressed_image
        self.preProcessImages(scale,x,y)
        self.clicked = False
        self.rect = self.idle_image.get_rect(center = (x,y))

    def preProcessImages(self, scale,x,y):

        width = self.idle_image.get_width()
        height = self.idle_image.get_height()
        self.idle_image = pygame.transform.scale(self.idle_image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(self.hover_image, (int(width * scale), int(height * scale)))
        self.pressed_image = pygame.transform.scale(self.pressed_image, (int(width * scale), int(height * scale)))
        self.idle_image.set_colorkey((0,0,0))
        self.hover_image.set_colorkey((0,0,0))
        self.pressed_image.set_colorkey((0,0,0))

    def draw(self, surface):
        action = False
        mouse_over = self.isMouseOver()
        if mouse_over:
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
