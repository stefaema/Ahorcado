from spriteSheet import SpriteSheet
import pygame

class Animation():
    def __init__(self, screen, delayPerFrame, spriteSheetPath, initialPos = [0,0], scale = 1):
        self.screen = screen
        self.current_frame = 0
        self.delayCounter = 0
        self.delayPerFrame = delayPerFrame
        self.spriteSheet = SpriteSheet(spriteSheetPath, scale)
        self.animationFrames = self.spriteSheet.get_images()
        self.x = initialPos[0]
        self.y = initialPos[1]
    def update(self):

        self.delayCounter += 1
        if self.delayCounter % self.delayPerFrame == 0:
            self.current_frame += 1
            if self.current_frame >= len(self.animationFrames):
                self.current_frame = 0

    def draw(self):
        pass

class SteadyAnimation(Animation):
    def __init__(self, screen, delayPerFrame, spriteSheetPath, initialPos, scale):
        super().__init__(screen, delayPerFrame, spriteSheetPath, initialPos, scale)
        self.Rects = [self.animationFrames[i].get_rect(center=(self.x, self.y)) for i in range(len(self.animationFrames))]
    
    def update(self):
        super().update()

    def draw(self):
        self.screen.blit(self.animationFrames[self.current_frame], self.Rects[self.current_frame])

class MovingAnimation(Animation):
    def __init__(self, screen, delayPerFrame, spriteSheetPath, initialPos, finalPos, movingTime, scale):
        super().__init__(screen, delayPerFrame, spriteSheetPath, initialPos, scale)
        self.initialX = initialPos[0]
        self.initialY = initialPos[1]
        self.finalX = finalPos[0]
        self.finalY = finalPos[1]
        self.movingTime = movingTime
        # Convierto segundos a cantidad total de cambio de frames
        self.total_updates = (movingTime * 60)//self.delayPerFrame 
        self.xPerUpdate = (self.finalX - self.initialX)//self.total_updates
        self.yPerUpdate = (self.finalY - self.initialY)//self.total_updates

    def update(self):
        super().update()
        if self.delayCounter % self.delayPerFrame == 0:
            self.current_frame += 1
            self.x += self.xPerUpdate
            self.y += self.yPerUpdate
        if self.x >= self.screen.get_width() - 1:
                self.x_pos = 0
        if self.y >= self.screen.get_height() - 1:
                self.y_pos = 0
    def draw(self):
        rect = self.animationFrames[self.current_frame].get_rect(center=(self.x, self.y))
        self.screen.blit(self.animationFrames[self.current_frame], rect)

class LoadingAnimation():
    def __init__(self, screen, animationTime, initialXPos = 0,lastXPos = -1, delayPerFrame = 4, imageScale = 1):
        self.screen = screen
        self.imageScale = imageScale
        # Load the sprite sheet and get the images
        sprite_sheet = SpriteSheet('Images/HangManWalking/HangManWalking.png',self.imageScale, 5, 1)
        self.loadingImages = sprite_sheet.get_images()
        self.delayPerFrame = delayPerFrame
        # Set the colorkey for each image (black = transparent)
        for image in self.loadingImages:
            image.set_colorkey((0, 0, 0))  

        self.sound = pygame.mixer.Sound('Sounds/steppingOnGrass.wav')
        self.sound.set_volume(0.6)
        self.sound.play()
        # Initialize the current frame index, frame delay counter, and x position
        self.current_frame = 0
        self.frame_delay = 0
        self.x_pos = initialXPos

        if lastXPos == -1:
            self.last_x_pos = self.screen.get_width() - 1
        else:
            self.last_x_pos = lastXPos

        # Calculate the number of updates before switching to the main menu
        self.total_updates = (animationTime * 60)//self.delayPerFrame 
        self.xPerUpdate = (self.last_x_pos - initialXPos) // self.total_updates
    def update(self):
        # Update the frame delay counter and current frame index
        self.frame_delay += 1

        if(self.last_x_pos - self.x_pos < self.xPerUpdate):
            self.sound.stop()
        if self.frame_delay % self.delayPerFrame == 0:
            self.current_frame += 1
            self.x_pos += self.xPerUpdate

            if self.current_frame >= len(self.loadingImages):
                self.current_frame = 0
            if self.x_pos >= self.screen.get_width() - 1:
                self.x_pos = 0

    def draw(self):
        rect = self.loadingImages[self.current_frame].get_rect(center=(self.x_pos, self.screen.get_height() - 320 * self.imageScale))
        self.screen.blit(self.loadingImages[self.current_frame], rect)


