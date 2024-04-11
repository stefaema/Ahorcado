from animations import SteadyAnimation
class SteadyCharacter():
    def __init__(self,screen, healthLost = 0, states = 7,delayPerFrame = 15,position = (923, 556),hangmanScale = 0.6):
        self.healthLost = healthLost
        self.animations_buffer = [SteadyAnimation(screen,delayPerFrame,f"Images/HangMan{i}/HangMan{i}.png",position,hangmanScale) for i in range(states)]
    
    def update(self,hasLostHealth = False):
        self.animations_buffer[self.healthLost].update()
        if hasLostHealth:
            if self.healthLost < len(self.animations_buffer) - 1:
                self.healthLost += 1
            else:
                self.healthLost = 0

            
    def draw(self):
        self.animations_buffer[self.healthLost].draw()