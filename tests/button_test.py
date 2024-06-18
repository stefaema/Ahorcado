import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame
from unittest.mock import MagicMock, patch
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        with patch.object(Button, 'preProcessImages', return_value=None), patch.object(Button, 'validate_parameters', return_value=None):
            self.button = Button(0, 0, MagicMock(), MagicMock(), MagicMock(), 1)
            self.button.preProcessImages = MagicMock()


    def test_idle(self):
        self.button.isMouseOver = MagicMock(return_value=False)
        self.button.isMousePressed = MagicMock(return_value=False)
        actionToDo = self.button.draw(MagicMock())
        self.assertFalse(self.button.clicked)
        self.assertEqual(self.button.image, self.button.idle_image)
        self.assertFalse(actionToDo)
        

    def test_hovered(self):
        self.button.isMouseOver = MagicMock(return_value=True)
        self.button.isMousePressed = MagicMock(return_value=False)
        actionToDo = self.button.draw(MagicMock())
        self.assertFalse(self.button.clicked)
        self.assertEqual(self.button.image, self.button.hover_image)
        self.assertFalse(actionToDo)

    def test_pressed(self):
        self.button.isMouseOver = MagicMock(return_value=True)
        self.button.isMousePressed = MagicMock(return_value=True)
        actionToDo = self.button.draw(MagicMock())
        self.assertTrue(self.button.clicked)
        self.assertEqual(self.button.image, self.button.pressed_image)
        self.assertTrue(actionToDo)

    def test_released(self):
        self.button.isMouseOver = MagicMock(return_value=False)
        self.button.isMousePressed = MagicMock(return_value=False)
        self.button.clicked = True
        actionToDo = self.button.draw(MagicMock())
        self.assertFalse(self.button.clicked)
        self.assertEqual(self.button.image, self.button.idle_image)
        self.assertFalse(actionToDo)

    def test_correct_init(self):
        surface = pygame.surface.Surface((1,1))
        try:
            button = Button(0, 0, surface, surface, surface, 1)
        except ValueError:
            self.fail("Button constructor raised ValueError unexpectedly!")
    def test_incorrect_init_scale(self):
        surface = pygame.surface.Surface((1,1))
        with self.assertRaises(ValueError):
            button = Button(0, 0, surface, surface, surface, surface)
    def test_incorrect_init_x(self):
        surface = pygame.surface.Surface((1,1))
        with self.assertRaises(ValueError):
            button = Button("0", 0, surface, surface, surface, 1)
    def test_incorrect_init_y(self):
        surface = pygame.surface.Surface((1,1))
        with self.assertRaises(ValueError):
            button = Button(0, "0", surface, surface, surface, 1)
    def test_incorrect_init_idle_image(self):
        surface = pygame.surface.Surface((1,1))
        with self.assertRaises(ValueError):
            button = Button(0, 0, "surface", surface, surface, 1)
    def test_incorrect_init_hover_image(self):
        surface = pygame.surface.Surface((1,1))
        with self.assertRaises(ValueError):
            button = Button(0, 0, surface, "surface", surface, 1)
    def test_incorrect_init_pressed_image(self):
        surface = pygame.surface.Surface((1,1))
        with self.assertRaises(ValueError):
            button = Button(0, 0, surface, surface, "surface", 1)

        

if __name__ == '__main__':
    unittest.main()