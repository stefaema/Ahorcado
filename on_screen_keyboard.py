import pygame
from text_to_image import TextToImageTool
from button import Button
class KeyOnScreen:
    def __init__(self, x, y, key, font_path, font_size, initial_color,transition_color,final_color, image_background, scale):
        self.x = x
        self.y = y
        self.letter = key
        self.image_background = image_background
        image_idle = TextToImageTool(x, y, key, font_path, font_size, initial_color, image_background).get_image(0.15)
        image_hover = TextToImageTool(x, y, key, font_path, font_size, transition_color,image_background).get_image(0.15)
        self.image_pressed = TextToImageTool(x, y, key, font_path, font_size, final_color, image_background).get_image(0.15)
        self.button = Button(x, y, image_idle, image_hover, self.image_pressed, scale)
        self.static = False
    def draw(self, surface):
        if not self.static:
            action = self.button.draw(surface)
            self.static = action
            return action
        else:
            surface.blit(self.image_pressed, self.image_pressed.get_rect(center=(self.x, self.y)))
    def get_letter(self):
        return self.letter
            
class KeyboardOnScreen:
    def __init__(self, screen, font_path, image_background, secret_word, scale =1):
        secret_word = secret_word.upper()
        self.image_background = image_background

        self.current_word = ["[] " for _ in range(len(secret_word))]

        self.keys = []
        self.correct_keys = []
        self.secret_word = secret_word
        self.incorrect_keys = []
        self.mistakes = 0

        def isKeyCorrect(key):
            return key in secret_word
        
        self.letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.start_x, self.start_y = 50, 400
        for i, letter in enumerate(self.letters):
            x = self.start_x + (50 + 10) * (i % 9)
            y = self.start_y + (50 + 10) * (i // 9)
            final_color = (255,0,0) if not isKeyCorrect(letter) else (0,255,0)
            key = KeyOnScreen(x, y,letter, font_path, 24, (255, 255, 255), (155, 155, 155), final_color, self.image_background, scale)
            self.keys.append(key)
            self.correct_keys.append(key) if isKeyCorrect(letter) else self.incorrect_keys.append(key)
        self.screen = screen

    def draw(self):
        incorrect_action = False
        correct_action = False
        for key in self.incorrect_keys:
            action = key.draw(self.screen)
            if action:
                self.mistakes += 1
                incorrect_action = True
            key.draw(self.screen)
        for key in self.correct_keys:
            action = key.draw(self.screen)
            if action:
                self.update_current_word(key)
                correct_action = True
        return incorrect_action , correct_action


    def update_current_word(self, key):
        indexes = [i for i, letter in enumerate(self.secret_word) if letter == key.get_letter()]
        for index in indexes:
            self.current_word[index] = " "+key.get_letter()+" "

    def get_current_word(self):
        return "".join(self.current_word)
    def did_win(self):
        current_word=self.get_current_word().upper()
        current_word = current_word.replace(" ","")
        if current_word == self.secret_word:
            return True
    def handle_mistakes(self):
        if self.mistakes == 0:
            return False
        else:
            self.mistakes -= 1
            return True