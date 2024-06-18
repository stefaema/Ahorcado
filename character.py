from animations import Animation, NoMovementStrategy
from sprite_sheet import SpriteSheet
import pygame
class CharacterState:
    def __init__(self, screen, delayPerFrame, imagePath, position, scale):
        self.sprite_sheet = SpriteSheet("320x320",imagePath)
        self.animation = Animation(screen, delayPerFrame, self.sprite_sheet,NoMovementStrategy(position), scale)

    def update(self):
        self.animation.update()

    def draw(self):
        self.animation.draw()

class Character:
    # Optimized for Hango
    def validate_parameters(self, screen, healthLost, states, delayPerFrame, position, hangmanScale):
        if not isinstance(screen, pygame.Surface):
            raise ValueError("Screen must be a pygame.Surface object")
        if not isinstance(healthLost, int):
            raise ValueError("Health lost must be an integer")
        if not isinstance(states, int):
            raise ValueError("States must be an integer")
        if not isinstance(delayPerFrame, int):
            raise ValueError("Delay per frame must be an integer")
        if not isinstance(position, tuple):
            raise ValueError("Position must be a tuple")
        if not isinstance(hangmanScale, (int, float)):
            raise ValueError("Hangman scale must be an integer or a float")
        
    def __init__(self, screen, healthLost=0, states=7, delayPerFrame=15, position=(923, 556), hangmanScale=0.7):
        self.validate_parameters(screen, healthLost, states, delayPerFrame, position, hangmanScale)
        self.healthLost = healthLost
        self.states = [CharacterState(screen, delayPerFrame, f"Images/HangMan{i}/HangMan{i}.png", position, hangmanScale) for i in range(states)]

    def update(self, hasLostHealth=False):
        self.states[self.healthLost].update()
        if hasLostHealth:
            self.healthLost = (self.healthLost + 1) % len(self.states)

    def draw(self):
        self.states[self.healthLost].draw()

    def did_lose(self):
        return self.healthLost == len(self.states) - 1