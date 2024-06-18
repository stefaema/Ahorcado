import sys
import os
import unittest
import pygame
from unittest.mock import MagicMock, patch

# Añade la ruta del directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos la clase
from text_to_image import TextToImageTool

class TestTextToImageTool(unittest.TestCase):
    def setUp(self):
        with patch.object(TextToImageTool, 'validate_params', return_value = None):
            pygame.init()
            self.font_path = 'fonts/PixeloidSansBold.ttf'
            self.image_background = MagicMock()
            self.text_tool = TextToImageTool(400, 300, "Hello, World!\nThis is a test.", self.font_path, 48, (255, 255, 255), background_surface=self.image_background)
            self.valid_args = {
                'x': 100,
                'y': 100,
                'text': "Sample Text",
                'font_path': "fonts/PixeloidSansBold.ttf",
                'font_size': 24,
                'font_color': (255, 255, 255),
                'background_surface': pygame.image.load('Images/Props/xd.png'),
                'line_spacing': 4
            }
    def test_initial_state(self):
        self.assertEqual(self.text_tool.text, "Hello, World!\nThis is a test.")
        self.assertEqual(self.text_tool.x, 400)
        self.assertEqual(self.text_tool.y, 300)
        self.assertEqual(self.text_tool.font_color, (255, 255, 255))
        self.assertEqual(self.text_tool.line_spacing, 4)

    def test_update_text(self):
        new_text = "New text"
        self.text_tool.update_text(new_text)
        self.assertEqual(self.text_tool.text, new_text)

    def test_draw_without_background(self):
        self.text_tool.background_surface = None
        mock_surface = MagicMock()
        self.text_tool.draw(mock_surface)
        self.assertTrue(mock_surface.blit.called)

    def test_draw_with_background(self):
        mock_surface = MagicMock()
        self.text_tool.draw(mock_surface)
        self.assertTrue(mock_surface.blit.called)

    def test_get_image_without_background(self):
        self.text_tool.background_surface = None
        image = self.text_tool.get_image()
        self.assertIsInstance(image, pygame.Surface)

    def test_get_image_with_background(self):
        with patch.object(TextToImageTool, 'scale_image', return_value = pygame.surface.Surface((1,1))):
            image = self.text_tool.get_image()
            self.assertIsInstance(image, pygame.Surface)


    # # Casos negativos
    def test_draw_with_invalid_font_path(self):
        with self.assertRaises(FileNotFoundError):
            invalid_font_tool = TextToImageTool(400, 300, "Invalid Font Path", "invalid_font.ttf", 48, (255, 255, 255))
            mock_surface = MagicMock()
            invalid_font_tool.draw(mock_surface)

    def test_get_image_with_empty_text(self):
        self.text_tool.update_text("")
        with patch.object(TextToImageTool, 'scale_image', return_value = pygame.surface.Surface((0,0))):
            image = self.text_tool.get_image()
            self.assertIsInstance(image, pygame.Surface)
        self.assertEqual(image.get_width(), 0)
        self.assertEqual(image.get_height(), 0)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['x'] = 'Invalid'
            self.text_tool.validate_params(**args)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['y'] = 'Invalid'
            self.text_tool.validate_params(**args)

    def test_invalid_text(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['text'] = 123
            self.text_tool.validate_params(**args)
    
    def test_invalid_font_path(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['font_path'] = 123
            self.text_tool.validate_params(**args)

    def test_invalid_font_size(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['font_size'] = 'Invalid'
            self.text_tool.validate_params(**args)
    
    def test_invalid_font_color(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['font_color'] = 'Invalid'
            self.text_tool.validate_params(**args)

    def test_invalid_background_surface(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['background_surface'] = 'Invalid'
            self.text_tool.validate_params(**args)
    
    def test_invalid_line_spacing(self):
        with self.assertRaises(ValueError):
            args = self.valid_args.copy()
            args['line_spacing'] = 'Invalid'
            self.text_tool.validate_params(**args)

if __name__ == '__main__':
    unittest.main()
