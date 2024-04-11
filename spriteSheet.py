import pygame
class SpriteSheet:
    def __init__(self, filename, scale = 1, cols = -1, rows= -1, pixelsPerCellX = 320, pixelsPerCellY = 320):
        self.sheet = pygame.image.load(filename).convert_alpha()
        
        if cols == -1 and rows == -1:
            cols = self.sheet.get_width()//pixelsPerCellX
            rows = self.sheet.get_height()//pixelsPerCellY
        
        self.cols = cols
        self.rows = rows
        self.cell_scale = scale
        self.rect = self.sheet.get_rect()

        w = self.cell_width = self.rect.width // self.cols
        h = self.cell_height = self.rect.height // self.rows
        self.cell_center = (w / 2, h / 2)

        self.cells = list([(index % self.cols * w, index // self.cols * h, w, h) for index in range(self.cols * self.rows)])

    def get_images(self):
        images = []
        for cell in self.cells:
            image = pygame.Surface((self.cell_width, self.cell_height)).convert_alpha()
            image.blit(self.sheet, (0, 0), cell)
            scaled_image = pygame.transform.scale(image, (int(self.cell_width * self.cell_scale), int(self.cell_height * self.cell_scale)))
            scaled_image.set_colorkey((0, 0, 0))  
            images.append(scaled_image)
        return images