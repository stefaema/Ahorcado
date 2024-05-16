import pygame

class InputBox:

    def __init__(self, image, pos_center, text='', COLOR_INACTIVE=pygame.Color('lightskyblue3'), COLOR_ACTIVE=pygame.Color('dodgerblue2')):
        self.image = image
        self.rect = self.image.get_rect(center=pos_center)
        self.rect.width //= 2
        self.rect.height = 32
        self.rect.x += self.image.get_width() // 4
        self.rect.y += self.image.get_width() // 4
        

        self.image_rect = self.image.get_rect(center=pos_center)
        self.color = COLOR_INACTIVE
        self.text = text
        self.blinking_cursor = "|"
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.COLOR_INACTIVE = COLOR_INACTIVE
        self.COLOR_ACTIVE = COLOR_ACTIVE
        self.blink_factor = 15
        self.blink_counter= 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isMouseOver():
                self.active = not self.active
            else:
                self.active = False
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def isMouseOver(self):
        isMouseOver = self.rect.collidepoint(pygame.mouse.get_pos())
        return isMouseOver
    
    def isMousePressed(self):
        isMousePressed = pygame.mouse.get_pressed()[0] == 1
        return isMousePressed
    def blink_cursor(self):
        if not self.active:
            self.blinking_cursor = ""
        else:
            if self.blink_counter == self.blink_factor:
                self.blinking_cursor = "|" if self.blinking_cursor == "" else ""
            self.blink_counter = (self.blink_counter + 1) % (self.blink_factor + 1)

    def update(self):
        self.blink_cursor()
        self.txt_surface = self.font.render(self.text + self.blinking_cursor, True, self.color)

    def activate(self):
        self.active = True
        self.color = self.COLOR_ACTIVE

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

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
        SCREEN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            input_box1.handle_event(event)
        input_box1.update()
        input_box1.draw(SCREEN)
        pygame.display.flip()
        CLOCK.tick(30)