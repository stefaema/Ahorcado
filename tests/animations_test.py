import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from animations import Animation, LinearStraightMovementStrategy

import unittest

from unittest.mock import MagicMock

class TestAnimation(unittest.TestCase):
    def setUp(self):
        self.screen = MagicMock()
        self.sprite_sheet = MagicMock()
        self.sprite_sheet.get_images.return_value = [MagicMock() for _ in range(5)]
        self.animation = Animation(self.screen, 10, self.sprite_sheet, (0, 0), (100, 100), 1)

    def test_update_frame(self):
        self.animation.movement_strategy= MagicMock()
        self.assertEqual(self.animation.current_frame, 0)
        self.animation.delay_counter = 10
        self.animation.update_frame()
        self.assertEqual(self.animation.current_frame, 1)

    def test_update_position(self):
        strategy = MagicMock()
        strategy.update_position = MagicMock()
        self.animation.movement_strategy = strategy
        self.animation.update_position()
        strategy.update_position.assert_called_once_with(self.animation)
    
    def test_draw(self):
        self.animation.current_frame = 1
        self.animation.x = 10
        self.animation.y = 10
        self.animation.draw()
        self.screen.blit.assert_called_once()
        
        

class TestLinearStraightMovementStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = LinearStraightMovementStrategy((0, 0), (100, 100), 1)

    def test_calculate_updates(self):
        self.assertEqual(self.strategy.x_per_update, 100/60)
        self.assertEqual(self.strategy.y_per_update, 100/60)
        self.assertEqual(self.strategy.total_updates, 60)

    def test_update_position(self):
        animation = MagicMock()
        animation.x = 0
        animation.y = 0
        animation.screen.get_width.return_value = 800
        animation.screen.get_height.return_value = 600
        self.strategy.update_position(animation)
        self.assertEqual(animation.x, 100/60)
        self.assertEqual(animation.y, 100/60)
    
    def test_update_position_overflow(self):
        animation = MagicMock()
        animation.x = 800
        animation.y = 600
        animation.screen.get_width.return_value = 800
        animation.screen.get_height.return_value = 600
        self.strategy.update_position(animation)
        self.assertAlmostEqual(animation.x, 100/60)
        self.assertAlmostEqual(animation.y, 100/60)

    def test_without_movement(self):
        animation = MagicMock()
        animation.screen.get_width.return_value = 800
        animation.screen.get_height.return_value = 600
        strategy_no_movement = LinearStraightMovementStrategy((0, 0), (0, 0), 1)
        animation.x = 0
        animation.y = 0
        strategy_no_movement.update_position(animation)
        self.assertEqual(animation.x, 0)
        self.assertEqual(animation.y, 0)



if __name__ == '__main__':
    unittest.main()

