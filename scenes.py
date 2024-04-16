import pygame
from button import Button
import time
from animations import *
from spriteSheet import SpriteSheet
from steadyCharacter import SteadyCharacter
class Scene:
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Crea un botón con los parámetros dados
    def create_button(self,xPos,yPos,idle,hover,pressed,scale):
        idle_image = pygame.image.load(idle)
        hover_image = pygame.image.load(hover)
        pressed_image = pygame.image.load(pressed)
        return Button(xPos, yPos, idle_image, hover_image, pressed_image, scale)

    def create_button2(self,xPos,yPos,path,scale):
        sheet = SpriteSheet(path,scale)
        images = sheet.get_images()
        return Button(xPos, yPos, images[0], images[1], images[2], scale)
    def update(self):
        pass

    def draw(self):
        pass           

class LoadingScene(Scene):
    def __init__(self, screen,loadingTime = 5):
        super().__init__(screen)
        font = pygame.font.Font('bitout.ttf', 90)
        self.text_surface = font.render('ahorcado', True, (1, 1, 1))
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.start_time = time.time()
        self.load_time = loadingTime

        delayPerFrame = 6
        #MovingAnimation no tiene sonido aun. TODO: Agregar sonido a MovingAnimation TODO: Realizar SoundManager
        self.loadingAnimation = LoadingAnimation(screen, self.load_time, (self.screen.get_width() - 1)//4,((self.screen.get_width() - 1)*3)//4, delayPerFrame, 0.8)
        self.loadingAnimation2 = MovingAnimation(screen, delayPerFrame, "Images/HangManWalking/HangManWalking.png",( (self.screen.get_width() - 1)//4, self.screen.get_height() - 320 ), ((3*(self.screen.get_width() - 1))//4 , self.screen.get_height() - 320), loadingTime, 0.8)


    def update(self):
        if time.time() - self.start_time > self.load_time:
            return MainMenuScene(self.screen)

        self.loadingAnimation.update()
        

    def draw(self):
        self.screen.fill((204, 236, 239))
        self.screen.blit(self.text_surface, self.text_rect)
        self.loadingAnimation.draw()
        

class MainMenuScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.textPlotImage = pygame.image.load('Images/Props/textPlotImage.png')
        self.textPlotImage = pygame.transform.scale(self.textPlotImage, (self.textPlotImage.get_width() * 0.7, self.textPlotImage.get_height() * 0.7))
        self.textPlotImage_rect = self.textPlotImage.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40))

        self.background = pygame.image.load('Images/Backgrounds/hangman-empty-background.png')
        self.background = pygame.transform.scale(self.background, (screen.get_width(), self.background.get_height() * screen.get_width() // self.background.get_width()))
        
        
        self.playButton = self.create_button((screen.get_width()) // 2, ((3*screen.get_height()) // 4)-20, 'Images/Props/playButtonIdle.png', 'Images/Props/playButtonHover.png', 'Images/Props/playButtonPressed.png', 0.5)
        self.playButtonIsClicked = False

    def update(self):
        if self.playButtonIsClicked:
            return PvPGameScene(self.screen)
        
    def draw(self):
        self.screen.fill((204, 236, 239))
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.textPlotImage, self.textPlotImage_rect)
        self.playButtonIsClicked = self.playButton.draw(self.screen)
        

class PvPGameScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.background = pygame.image.load('Images/Backgrounds/hangman-structured-background.png')
        self.background = pygame.transform.scale(self.background, (screen.get_width(), self.background.get_height() * screen.get_width() // self.background.get_width()))
        #self.silhouetteAnimation = SteadyAnimation(screen, 6, 'Images/Silhouette/Silhouette.png', (100, (screen.get_height() - 1) - 100), 1) 

        delayPerFrameHangman = 40
        positionHangman = (923, 556)
        hangmanScale = 0.6
        self.hangMan = SteadyCharacter(screen,0,7,delayPerFrameHangman,positionHangman,hangmanScale)

        self.testButton = self.create_button2(positionHangman[0], positionHangman[1] + 150, 'Images/Props/testButton.png', 0.5)

        self.testButtonAction = False
    def update(self):
        self.hangMan.update()
        if self.testButtonAction:
            self.hangMan.update(True)
        else:
            self.hangMan.update(False)
        #self.silhouetteAnimation.update()
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.hangMan.draw()
        #self.silhouetteAnimation.draw()
        self.testButtonAction = self.testButton.draw(self.screen)