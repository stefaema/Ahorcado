import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock, patch
from loading_scene import LoadingScene


class TestLoadingScene(unittest.TestCase):
    def setUp(self):
        with patch.object(LoadingScene, 'build_text_surface', return_value=(MagicMock(), MagicMock())), patch.object(LoadingScene, 'build_loading_animation', return_value=MagicMock()):
            self.screen = MagicMock()
            self.sound_mixer = MagicMock()
            self.clock = MagicMock()
            self.loading_scene = LoadingScene(self.screen, self.sound_mixer, self.clock, 2)
    def test_initial_state(self):
        self.assertEqual(self.loading_scene.loading_time, 2)
        self.assertEqual(self.loading_scene.delay_per_frame, 8)
    def test_update(self):
        with patch.object(LoadingScene, 'change_animation'):
            self.loading_scene.update()
            self.sound_mixer.stop.assert_not_called()
            self.assertEqual(self.loading_scene.animation.update.call_count, 1)
    def test_update_return(self):
        with patch.object(LoadingScene, 'get_elapsed_time', return_value=self.loading_scene.loading_time + 1), patch.object(LoadingScene, 'return_next_scene', return_value=MagicMock()), patch.object(LoadingScene, 'change_animation') as change_animation:
            return_value = self.loading_scene.update()
            self.sound_mixer.stop.assert_called_once()
            self.loading_scene.return_next_scene.assert_called_once()


if __name__ == '__main__':
    unittest.main()