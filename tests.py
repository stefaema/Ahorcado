import unittest
from unittest.mock import MagicMock, patch
from button import Button
from spriteSheet import SpriteSheet
import pygame
import xmlrunner

class TestButton(unittest.TestCase):
    #Setup de la prueba del botón
    def setUp(self):
        pygame.init()
        self.button = Button(100, 100, pygame.image.load('Images/Props/playButtonIdle.png'), pygame.image.load('Images/Props/playButtonHover.png'), pygame.image.load('Images/Props/playButtonPressed.png'), 0.5)
        self.mock_rect = MagicMock()
        self.mock_surface = MagicMock()
    def test_draw(self):
        surface = MagicMock()
        self.button.draw(surface)
        surface.blit.assert_called_once()

    
    #Prueba encimar el puntero en el botón (hover)
    def test_button_hover(self):
        surface = MagicMock()
        mock_rect = MagicMock()
        self.button.rect = self.mock_surface
        self.button.rect.collidepoint.return_value = True
        self.button.draw(surface)
        self.assertEqual(self.button.image, self.button.hover_image)

    #Prueba de presionar el botón
    @patch('pygame.mouse.get_pressed', return_value=(1,0,0))
    def test_button_pressed(self, _):
        surface = MagicMock()
        mock_rect = MagicMock()
        self.button.rect = self.mock_surface
        self.button.rect.collidepoint.return_value = True
        botonAcciona = self.button.draw(surface)
        self.assertEqual(self.button.image, self.button.pressed_image)
        self.assertTrue(self.button.clicked)
        self.assertTrue(botonAcciona)
        
    #Prueba de soltar el botón
    @patch('pygame.mouse.get_pressed', return_value=(0,0,0))
    def test_button_released(self, _):
        surface = MagicMock()
        mock_rect = MagicMock()
        self.button.rect = self.mock_surface
        self.button.rect.collidepoint.return_value = True
        self.button.clicked = True
        self.button.draw(surface)
        self.assertFalse(self.button.clicked)

    # Prueba idle del botón
    @patch('pygame.mouse.get_pressed', return_value=(0,0,0))
    def test_button_no_interaction(self, _):
        surface = MagicMock()
        mock_rect = MagicMock()
        self.button.rect = self.mock_surface
        self.button.rect.collidepoint.return_value = False
        self.button.draw(surface)
        self.assertFalse(self.button.clicked)

    # Prueba de clic fuera del botón
    @patch('pygame.mouse.get_pressed', return_value=(1,0,0))
    def test_button_click_outside(self, _):
        surface = MagicMock()
        mock_rect = MagicMock()
        self.button.rect = self.mock_surface
        self.button.rect.collidepoint.return_value = False
        self.button.draw(surface)
        self.assertFalse(self.button.clicked)

class TestSpriteSheet(unittest.TestCase):

    #Setup de la prueba de sprite sheet
    def setUp(self):
        pygame.init()

    #Prueba de la creación con parametros de columnas y filas
    @patch('pygame.image.load', return_value=MagicMock())
    @patch('pygame.Surface', return_value=MagicMock())
    @patch('pygame.transform', return_value=MagicMock())
    def test_get_images_0(self, _, __, ___):
        self.spriteSheet = SpriteSheet(MagicMock(), 0.5, 3, 3)
        self.assertEqual(len(self.spriteSheet.get_images()), 9)
    

    #Prueba de la creación sin parametros de columnas y filas
    @patch('pygame.image.load', return_value=MagicMock())
    @patch('pygame.Surface', return_value=MagicMock())
    @patch('pygame.transform', return_value=MagicMock())
    def test_get_images_1(self, mockSheet, __, ___):
        self.spriteSheet = SpriteSheet(MagicMock(), 0.5)
        self.spriteSheet.sheet.get_width.return_value = 640
        self.spriteSheet.sheet.get_height.return_value = 640
        self.spriteSheet.calculate_cols_and_rows(self.spriteSheet.sheet.get_width(), self.spriteSheet.sheet.get_height(), 320, 320)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))