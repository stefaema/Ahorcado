from animations import Animation, NoMovementStrategy
from sprite_sheet import SpriteSheet

class CharacterState:
    def __init__(self, screen, delayPerFrame, imagePath, position, scale):
        self.sprite_sheet = SpriteSheet("320x320",imagePath)
        self.animation = Animation(screen, delayPerFrame, self.sprite_sheet, position, position, 1, NoMovementStrategy(), scale)

    def update(self):
        self.animation.update()

    def draw(self):
        self.animation.draw()

class Character:
    # Optimized for Hango
    def __init__(self, screen, healthLost=0, states=7, delayPerFrame=15, position=(923, 556), hangmanScale=0.7):
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