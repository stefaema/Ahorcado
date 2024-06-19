import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock, patch
from word_pick_scene import WordPickScene

class TestWordPickScene(unittest.TestCase):
    def setUp(self):
        with patch.object(WordPickScene, 'build_subtitle',return_value=(MagicMock(),MagicMock())), patch.object(WordPickScene, 'build_warning_text',return_value=(MagicMock(),MagicMock(),MagicMock(),MagicMock())), patch.object(WordPickScene, 'build_input_box'), patch.object(WordPickScene, 'build_secure_input_toggle'), patch.object(WordPickScene, 'build_executioner_animation'), patch.object(WordPickScene, 'build_play_button'):
            self.word_pick_scene = WordPickScene(MagicMock(), MagicMock())
  
    def test_initial_values(self):
        self.assertEqual(self.word_pick_scene.ready_for_next_scene, False)
        self.assertEqual(self.word_pick_scene.secret_word, "")
    def test_update(self):
        self.word_pick_scene.play_button.draw.return_value = False
        self.word_pick_scene.draw()
        self.word_pick_scene.update()
        self.word_pick_scene.play_button.draw.assert_called_once()
        self.assertFalse(self.word_pick_scene.ready_for_next_scene)
    def test_update_returnin_scene(self):
        with patch.object(WordPickScene, 'return_next_scene', return_value=None):
            self.word_pick_scene.play_button.draw.return_value = True
            self.word_pick_scene.draw()
            self.word_pick_scene.update()
            self.word_pick_scene.play_button.draw.assert_called_once()
            self.word_pick_scene.return_next_scene.assert_called_once()
    def test_draw(self):
        self.word_pick_scene.draw()
        self.word_pick_scene.screen.blit.assert_called()
  
if __name__ == '__main__':
    unittest.main()