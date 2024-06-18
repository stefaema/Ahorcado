import pygame
from button import Button

# Assuming the Button class and its state classes are defined as provided

class LeverState:
    def draw(self, lever, surface):
        pass

class OnState(LeverState):
    def draw(self, lever, surface):
        if lever.on_off_button.draw(surface):
            lever.state = lever.offState
    def which_state(self):
        return True

class OffState(LeverState):
    def draw(self, lever, surface):
        if lever.off_on_button.draw(surface):
            lever.state = lever.onState
    def which_state(self):
        return False

class Lever:
    def validate_parameters(self, x, y, off_image, on_image, hover_off_image, hover_on_image, scale):
        if not isinstance(x, (int, float)):
            raise ValueError("x must be an integer or float")
        if not isinstance(y, (int, float)):
            raise ValueError("y must be an integer or float")
        if not all(isinstance(img, pygame.Surface) for img in [off_image, on_image, hover_off_image, hover_on_image]):
            raise ValueError("Image parameters must be pygame.Surface objects")
        if not isinstance(scale, (int, float)) or scale <= 0:
            raise ValueError("scale must be a positive integer or float")
        
    def __init__(self, x, y, off_image, on_image, hover_off_image,hover_on_image, scale):
        self.validate_parameters(x, y, off_image, on_image, hover_off_image, hover_on_image, scale)
        self.onState = OnState()
        self.offState = OffState()
        self.state = self.offState
        self.on_off_button = self.create_button(x, y, on_image, hover_on_image, off_image, scale)
        self.off_on_button = self.create_button(x, y, off_image, hover_off_image, on_image, scale)


        
    def create_button(self, x, y, idle,hover,pressed, scale):
        return Button(x, y, idle,hover,pressed, scale)
    
    def draw(self, surface):
        self.state.draw(self, surface)
    def toggled(self):
        return self.state.which_state()
