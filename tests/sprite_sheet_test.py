import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import MagicMock, patch
import pygame
from sprite_sheet import SpriteSheet

class TestSpriteSheet(unittest.TestCase):
    
    #Setup de la prueba de sprite sheet

    def setUp(self):
        
        pygame.init()

    def test_cell_dimensions(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((32, 32))):
            spriteSheet = SpriteSheet("32x32", MagicMock())
        self.assertEqual(spriteSheet.cell_width, 32)
        self.assertEqual(spriteSheet.cell_height, 32)

    def test_column_count(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((128, 32))):
            spriteSheet = SpriteSheet("32x32", MagicMock())
        self.assertEqual(spriteSheet.column_count, 4)

    def test_row_count(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((32, 128))):
            spriteSheet = SpriteSheet("32x32", MagicMock())
        self.assertEqual(spriteSheet.row_count, 4)

    def test_calculate_sprite_locations(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((128, 32))):
            spriteSheet = SpriteSheet("32x32", MagicMock())
        self.assertEqual(spriteSheet.calculate_sprite_locations(), [(0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32), (96, 0, 32, 32)])



    def test_get_images(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((128, 32))):
            spriteSheet = SpriteSheet("32x32", MagicMock())
        spriteSheet.calculate_sprite_locations()
        with patch.object(SpriteSheet, 'surface_generator', return_value=MagicMock()):
            self.assertEqual(len(spriteSheet.get_images()), 4)

    def test_raise_parameter_value_error(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((32, 32))):
            with self.assertRaises(ValueError):
                spriteSheet = SpriteSheet("3232", MagicMock())

    def test_divisibility_raise_value_error(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((33, 32))):
            with self.assertRaises(ValueError):
                spriteSheet = SpriteSheet("32x32", MagicMock())   
                spriteSheet.calculate_sprite_locations()
    
    def test_raise_invalid_cell_dimensions_error(self):
        with patch.object(SpriteSheet, 'image_loader', return_value=pygame.Surface((32, 32))):
            with self.assertRaises(ValueError):
                spriteSheet = SpriteSheet("0x32", MagicMock())

                
if __name__ == '__main__':
    unittest.main()    

