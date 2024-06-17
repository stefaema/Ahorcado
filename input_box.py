import pygame
from button import Button
import unicodedata
class verification_strategy:
    def verify(input_box):
        pass
    def criteria():
        pass
class standard_verification_strategy(verification_strategy):
    
    def verify(input_box):
        def eliminar_acentos(texto):
            texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
            texto = texto.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
            return texto
        # Eliminar acentos
        texto_sin_acentos = eliminar_acentos(input_box.text).lower()
        # Verificar que solo contiene letras del abecedario español
        abecedario = "abcdefghijklmnñopqrstuvwxyz"
        
        for caracter in texto_sin_acentos.lower():
            if caracter not in abecedario:
                return False
        
        # Verificar que no tiene espacios
        if ' ' in input_box.text:
            return False
        if not texto_sin_acentos.strip():
            return False
        
        input_box.text = texto_sin_acentos
        return True
    def criteria():
        return "Solo una palabra, sin espacios ni caracteres especiales"

class InputBox:

    def __init__(self, image, pos_center, text='', verification_strategy=standard_verification_strategy):
        self.normal_image = image
        self.image = self.normal_image
        self.rect = self.image.get_rect(center=pos_center)
        self.rect.width //= 1.2
        self.rect.height = self.rect.width // 2
        margin = (self.image.get_width() - self.rect.width) // 2
        self.rect.x += margin
        self.rect.y += self.image.get_width() // 16
        self.verification_strategy = verification_strategy        
        self.image_rect = self.image.get_rect(center=pos_center)
        self.text = text
        self.color = (0, 0, 0)
        self.blinking_cursor = "|"
        self.font = pygame.font.Font("fonts/PixeloidSansBold.ttf", 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.blink_factor = 15
        self.blink_counter= 0
        self.secure_text_entry = False
        self.raw_text_surface = self.font.render(text, True, self.color)
    def set_secure_text_entry(self, secure_text_entry):
        self.secure_text_entry = secure_text_entry

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < 15 and (event.key not in [pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_TAB, pygame.K_ESCAPE]):
                    self.text += event.unicode


    def isMouseOver(self):
        isMouseOver = self.rect.collidepoint(pygame.mouse.get_pos())
        return isMouseOver
    
    def verify(self):
        return self.verification_strategy.verify(self)



    def isMousePressed(self):
        isMousePressed = pygame.mouse.get_pressed()[0] == 1
        return isMousePressed
    def blink_cursor(self):
        if self.blink_counter == self.blink_factor:
            self.blinking_cursor = "|" if self.blinking_cursor == "" else ""
        self.blink_counter = (self.blink_counter + 1) % (self.blink_factor + 1)

    def update(self):
        self.blink_cursor()
        if self.secure_text_entry:
            self.secure_text = "*" * len(self.text)
        else:
            self.secure_text = self.text
        
        self.txt_surface = self.font.render(self.secure_text + self.blinking_cursor, True, self.color)
        self.raw_text_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)

        center_x= self.image_rect.centerx
        text_width = self.raw_text_surface.get_width()
        text_x = center_x - text_width // 2
        screen.blit(self.txt_surface, (text_x, self.rect.y+ self.image_rect.height//4))

    def get_text(self):
        return self.text
    def empty(self):
        self.text = ''
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Input Field Test")
    CLOCK = pygame.time.Clock()
    

    imagen = pygame.image.load("Images/Props/thinkin.png")
    pos = (1600/2, 900/2)
    imagen_rect = imagen.get_rect(center=pos)

    input_box1 = InputBox(imagen, (1600/2,900/2))
    while True:
        SCREEN.fill((0,1,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            input_box1.handle_event(event)
        input_box1.update()
        input_box1.draw(SCREEN)
        pygame.display.flip()
        CLOCK.tick(30)