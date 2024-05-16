import pygame
class InvalidCellDimensionsError(ValueError):
    pass

class InvalidSpriteSheetDimensionsError(ValueError):
    pass

class SpriteLocationStrategy:
    def calculate_sprite_locations(self, sprite_sheet):
        pass

class DefaultSpriteLocationStrategy(SpriteLocationStrategy):
    def calculate_sprite_locations(self, sprite_sheet):
        # Checks if the sprite sheet's dimensions are divisible by the cell's dimensions
        if sprite_sheet.sheet_image.get_width() % sprite_sheet.cell_width != 0 or sprite_sheet.sheet_image.get_height() % sprite_sheet.cell_height != 0:
            raise ValueError("The sprite sheet's dimensions must be divisible by the cell's dimensions")
        # Calculates the location of the upper left corner of each sprite in the sprite sheet
        sprite_x_locations = [x for x in range(0, sprite_sheet.sheet_image.get_width(), sprite_sheet.cell_width)]
        sprite_y_locations = [y for y in range(0, sprite_sheet.sheet_image.get_height(), sprite_sheet.cell_height)]
        return [(x, y, sprite_sheet.cell_width, sprite_sheet.cell_height) for x in sprite_x_locations for y in sprite_y_locations]


class SpriteSheet:
    def __init__(self, cell_dimensions, image_filename, location_strategy=DefaultSpriteLocationStrategy()):
        self.sheet_image = self.image_loader(image_filename)
        self._location_strategy = location_strategy
        # cell_dimensions is a string in the format '{width}x{height}'
        try:
            self.cell_width, self.cell_height = map(int, cell_dimensions.split('x'))
            if self.cell_width <= 0 or self.cell_height <= 0:
                raise InvalidCellDimensionsError(f"Cell dimensions must be positive integers, got {cell_dimensions}")
        except ValueError:
            raise InvalidCellDimensionsError(f"Cell dimensions must be in format 'widthxheight', got {cell_dimensions}")

        self.column_count = self.sheet_image.get_width() // self.cell_width
        self.row_count = self.sheet_image.get_height() // self.cell_height
        

    def get_images(self, scale=1):
        self.sprite_locations = self.calculate_sprite_locations()
        cell_images = []
        # Creates a surface for each sprite in the sprite sheet
        for sprite_location in self.sprite_locations:
            cell_images.append(self.surface_generator(sprite_location))
            if scale != 1:
                cell_images[-1] = pygame.transform.scale(cell_images[-1], (int(self.cell_width * scale), int(self.cell_height * scale)))
        return cell_images
    
    def surface_generator(self, sprite_location):
        cell_surface = pygame.Surface((self.cell_width, self.cell_height)).convert_alpha()
        cell_surface.blit(self.sheet_image, (0, 0), sprite_location)
        return cell_surface



    def image_loader(self, image_filename):
        return pygame.image.load(image_filename).convert_alpha()
    
    def calculate_sprite_locations(self):
        return self._location_strategy.calculate_sprite_locations(self)
    
    def set_location_strategy(self, location_strategy):
        self._location_strategy = location_strategy
    
