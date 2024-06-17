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
    def __init__(self, x, y, off_image, on_image, hover_off_image,hover_on_image, scale):
        self.onState = OnState()
        self.offState = OffState()
        self.state = self.offState
        self.on_off_button = Button(x, y, on_image, hover_on_image, off_image, scale)
        self.off_on_button = Button(x, y, off_image, hover_off_image, on_image, scale)

    def draw(self, surface):
        self.state.draw(self, surface)
    def toggled(self):
        return self.state.which_state()
# Example usage of the Lever class
def main():
    pygame.init()
    off_image_path = 'Images/Props/off_state.png'
    on_image_path = 'Images/Props/on_state.png'
    hover_on_image_path = 'Images/Props/hover_on_state.png'
    off_image = pygame.image.load(off_image_path)
    on_image = pygame.image.load(on_image_path)
    hover_off_image_path = 'Images/Props/hover_off_state.png'
    hover_on_image = pygame.image.load(hover_on_image_path)
    hover_off_image = pygame.image.load(hover_off_image_path)
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Lever Example")

    # Assuming off_image, on_image, and hover_image are defined similarly to the Button example
    lever = Lever(400, 300, off_image, on_image, hover_off_image, hover_on_image, 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        lever.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()