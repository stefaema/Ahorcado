import pygame
class TextToImageTool:
    def __init__(self, x, y, text, font_path, font_size, font_color, background_surface=None, line_spacing=4):
        self.text = text
        self.x = x
        self.y = y
        self.font = pygame.font.Font(font_path, font_size)
        self.font_color = font_color
        self.background_surface = background_surface
        self.line_spacing = line_spacing
        if self.background_surface:
            self.background_surface_rect = self.background_surface.get_rect(center=(self.x, self.y))
        else:
            self.background_surface_rect = None

    def update_text(self, text):
        self.text = text
    def draw(self, surface):
        lines = self.text.splitlines()
        line_height = self.font.get_height()
        total_height = (line_height + self.line_spacing) * len(lines) - self.line_spacing
        start_y = self.y - total_height // 2

        if self.background_surface and self.background_surface_rect:
            surface.blit(self.background_surface, self.background_surface_rect.topleft)

        for i, line in enumerate(lines):
            line_surface = self.font.render(line, True, self.font_color)
            line_width, line_height = line_surface.get_size()
            line_x = self.x - line_width // 2
            line_y = start_y + i * (line_height + self.line_spacing)
            surface.blit(line_surface, (line_x, line_y))

    def get_image(self,background_scale = 1):
        # Divide el texto en líneas
        lines = self.text.splitlines()
        
        # Obtiene la altura de cada línea
        line_height = self.font.get_height()
        # Calcula la altura total del texto con el espacio entre líneas
        total_height = (line_height + self.line_spacing) * len(lines) - self.line_spacing
        # Calcula el ancho total del texto, basado en la línea más larga
        total_width = max([self.font.size(line)[0] for line in lines])
        
        # Crea una superficie con capacidad para transparencia
        image = self.background_surface.copy() if self.background_surface else pygame.Surface((total_width, total_height), pygame.SRCALPHA)
        image = pygame.transform.scale(image, (int(image.get_width()*background_scale), int(image.get_height()*background_scale)))
        for i, line in enumerate(lines):
            # Renderiza cada línea de texto
            line_surface = self.font.render(line, True, self.font_color)
            line_width, line_height = line_surface.get_size()
            
            # Calcula la posición x e y para centrar cada línea en la superficie
            line_x = (total_width - line_width) // 2
            line_y = i * (line_height + self.line_spacing)
            
            # Dibuja cada línea de texto en la superficie 'image'
            image.blit(line_surface, (line_x+image.get_width()//2-line_surface.get_width()//2,line_y+image.get_height()//2-line_surface.get_height()//2))
        
        return image


def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Text to Image Test")

    clock = pygame.time.Clock()

    font_path = "fonts/PixeloidSansBold.ttf"
    image_background = pygame.image.load('Images/Props/xd.png')
    text = "Hello, World!\nThis is a test."
    text_image = TextToImageTool(screen_width // 2, screen_height // 2, text, font_path, 48, (255, 255, 255), background_surface=image_background)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))
        #text_image.draw(screen)

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()