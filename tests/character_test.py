import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import Mock, patch
from character import Character, CharacterState

class TestCharacter(unittest.TestCase):
    @patch('character.SpriteSheet', autospec=True)
    @patch('character.Animation', autospec=True)
    def setUp(self, mock_animation, mock_sprite_sheet):
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

if __name__ == '__main__':
    unittest.main()