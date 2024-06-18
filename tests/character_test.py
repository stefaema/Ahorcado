import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import Mock, patch
from character import Character, CharacterState
import pygame
class TestCharacter(unittest.TestCase):
    @patch('character.SpriteSheet', autospec=True)
    @patch('character.Animation', autospec=True)
    def setUp(self, mock_animation, mock_sprite_sheet):
        with patch.object(Character, 'validate_parameters', return_value=None):
            self.screen = Mock()
            self.character = Character(self.screen)

    def test_update_without_health_loss(self):
        self.character.update()
        self.assertEqual(self.character.healthLost, 0)

    def test_update_with_health_loss(self):
        self.character.update(hasLostHealth=True)
        self.assertEqual(self.character.healthLost, 1)

    def test_update_with_health_loss_at_max(self):
        self.character.healthLost = 6
        self.character.update(hasLostHealth=True)
        self.assertEqual(self.character.healthLost, 0)

    def test_draw(self):
        self.character.states = [Mock() for _ in range(7)]
        self.character.draw()
        self.character.states[0].draw.assert_called_once()
    
    def test_did_lose(self):
        self.character.healthLost = 6
        self.assertTrue(self.character.did_lose())
        self.character.healthLost = 0
        self.assertFalse(self.character.did_lose())
    def test_init_with_valid_parameters(self):
        try:
            self.character.validate_parameters(pygame.surface.Surface((1,1)), 0, 7, 15, (923, 556), 0.7)
        except ValueError:
            self.fail("Character constructor raised ValueError unexpectedly!")
    def test_init_with_invalid_surface(self):
        with self.assertRaises(ValueError):
            self.character.validate_parameters(1, 0, 7, 15, (923, 556), 0.7)
    def test_init_with_invalid_health_lost(self):
        with self.assertRaises(ValueError):
            self.character.validate_parameters(pygame.surface.Surface((1,1)), "0", 7, 15, (923, 556), 0.7)
    def test_init_with_invalid_states(self):
        with self.assertRaises(ValueError):
            self.character.validate_parameters(pygame.surface.Surface((1,1)), 0, "7", 15, (923, 556), 0.7)
    def test_init_with_invalid_delay_per_frame(self):
        with self.assertRaises(ValueError):
            self.character.validate_parameters(pygame.surface.Surface((1,1)), 0, 7, "15", (923, 556), 0.7)
    def test_init_with_invalid_position(self):
        with self.assertRaises(ValueError):
            self.character.validate_parameters(pygame.surface.Surface((1,1)), 0, 7, 15, 923, 0.7)
    def test_init_with_invalid_hangman_scale(self):
        with self.assertRaises(ValueError):
            self.character.validate_parameters(pygame.surface.Surface((1,1)), 0, 7, 15, (923, 556), "0.7")
if __name__ == '__main__':
    unittest.main()