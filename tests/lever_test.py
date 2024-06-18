import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import pygame
from unittest.mock import MagicMock, patch
from lever import Lever, OnState, OffState


class TestLever(unittest.TestCase):
    def setUp(self):
        # Mocking the Button class
        with patch.object(Lever, 'validate_parameters', return_value=None), patch.object(Lever, 'create_button', return_value=MagicMock()):
            pygame.init()
            # Create mock images
            self.off_image = MagicMock()
            self.on_image = MagicMock()
            self.hover_off_image = MagicMock()
            self.hover_on_image = MagicMock()
            
            self.lever = Lever(0, 0, self.off_image, self.on_image, self.hover_off_image, self.hover_on_image, 1)

    def test_initial_state(self):
        self.assertIsInstance(self.lever.state, OffState)
        self.assertFalse(self.lever.toggled())

    def test_toggle_to_on(self):
        # Mock the off_on_button to simulate a press
        self.lever.off_on_button.draw.return_value = True
        
        # Call draw to process the state change
        self.lever.draw(MagicMock())
        
        self.assertIsInstance(self.lever.state, OnState)
        self.assertTrue(self.lever.toggled())

    def test_toggle_to_off(self):
        # Set initial state to OnState
        self.lever.state = self.lever.onState
        
        # Mock the on_off_button to simulate a press
        self.lever.on_off_button.draw.return_value = True
        
        # Call draw to process the state change
        self.lever.draw(MagicMock())
        
        self.assertIsInstance(self.lever.state, OffState)
        self.assertFalse(self.lever.toggled())

    def test_validate_valid_parameters(self):
        try:
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, 0, image,image,image,image, 1)
        except ValueError:
            self.fail("validate_parameters() raised ValueError unexpectedly!")
    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters("0", 0, image,image,image,image, 1)
    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, "0", image,image,image,image, 1)
    def test_invalid_off_image(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, 0, "image",image,image,image, 1)
    def test_invalid_on_image(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, 0, image,"image",image,image, 1)
    def test_invalid_hover_off_image(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, 0, image,image,"image",image, 1)
    def test_invalid_hover_on_image(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, 0, image,image,image,"image", 1)
    def test_invalid_scale(self):
        with self.assertRaises(ValueError):
            image = pygame.surface.Surface((1,1))
            self.lever.validate_parameters(0, 0, image,image,image,image, "1")
if __name__ == '__main__':
    unittest.main()
