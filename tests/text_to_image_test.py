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
        pygame.init()
        self.font_path = 'fonts/PixeloidSansBold.ttf'
        self.image_background = MagicMock()
        self.text_tool = TextToImageTool(400, 300, "Hello, World!\nThis is a test.", self.font_path, 48, (255, 255, 255), background_surface=self.image_background)

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

    # def test_get_image_with_background(self):
    #     image = self.text_tool.get_image()
    #     self.assertIsInstance(image, pygame.Surface)

    # def test_get_image_scaled(self):
    #     scaled_image = self.text_tool.get_image(background_scale=0.5)
    #     self.assertEqual(scaled_image.get_width(), int(self.image_background.get_width() * 0.5))
    #     self.assertEqual(scaled_image.get_height(), int(self.image_background.get_height() * 0.5))

    # # Casos negativos
    def test_draw_with_invalid_font_path(self):
        with self.assertRaises(FileNotFoundError):
            invalid_font_tool = TextToImageTool(400, 300, "Invalid Font Path", "invalid_font.ttf", 48, (255, 255, 255))
            mock_surface = MagicMock()
            invalid_font_tool.draw(mock_surface)

    # def test_get_image_with_empty_text(self):
    #     self.text_tool.update_text("")
    #     image = self.text_tool.get_image()
    #     self.assertEqual(image.get_width(), 0)
    #     self.assertEqual(image.get_height(), 0)

    # def test_draw_with_empty_text(self):
    #     self.text_tool.update_text("")
    #     mock_surface = MagicMock()
    #     self.text_tool.draw(mock_surface)
    #     self.assertFalse(mock_surface.blit.called)


if __name__ == '__main__':
    unittest.main()
