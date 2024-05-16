import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame
from unittest.mock import MagicMock, patch
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        with patch.object(Button, 'preProcessImages', return_value=None):
            pygame.init()
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

if __name__ == '__main__':
    unittest.main()