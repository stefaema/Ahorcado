import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock, patch
from main_menu_scene import MainMenuScene

class TestLoadingScene(unittest.TestCase):
    def setUp(self):
        with patch.object(MainMenuScene, 'build_background', return_value=MagicMock()), patch.object(MainMenuScene, 'build_game_plot_image', return_value=MagicMock()), patch.object(MainMenuScene, 'build_play_button', return_value=MagicMock()), patch.object(MainMenuScene, 'return_next_scene', return_value=MagicMock()):
            self.screen = MagicMock()
            self.sound_mixer = MagicMock()
            self.main_menu_scene = MainMenuScene(self.screen, self.sound_mixer)
    def test_initial_state(self):
        self.assertEqual(self.main_menu_scene.ready_for_next_scene, False)
    def test_update(self):
        self.main_menu_scene.update()
        self.sound_mixer.play.assert_called_once()
    def test_update_return(self):
        with patch.object(MainMenuScene, 'return_next_scene', return_value=MagicMock()):
            return_value = self.main_menu_scene.update()
            self.sound_mixer.fade_out.assert_not_called()
            self.main_menu_scene.return_next_scene.assert_not_called()
            self.assertEqual(return_value, None)
        with patch.object(MainMenuScene, 'return_next_scene', return_value=MagicMock()):
            self.main_menu_scene.ready_for_next_scene = True
            return_value = self.main_menu_scene.update()
            self.sound_mixer.fade_out.assert_called_once()
            self.main_menu_scene.return_next_scene.assert_called_once()
            self.assertEqual(return_value, self.main_menu_scene.return_next_scene.return_value)
    def test_draw(self):
        with patch.object(MainMenuScene, 'draw_background', return_value=MagicMock()), patch.object(MainMenuScene, 'build_game_plot_image', return_value=MagicMock()), patch.object(MainMenuScene, 'build_play_button', return_value=MagicMock()):
            self.main_menu_scene.draw()
            self.main_menu_scene.draw_background.assert_called_once()
            self.main_menu_scene.text_plot.draw.assert_called_once()
            self.main_menu_scene.play_button.draw.assert_called_once()
    def test_draw_ready_for_next_scene(self):
        with patch.object(MainMenuScene, 'draw_background', return_value=MagicMock()), patch.object(MainMenuScene, 'build_game_plot_image', return_value=MagicMock()), patch.object(MainMenuScene, 'build_play_button', return_value=MagicMock()):
            self.main_menu_scene.ready_for_next_scene = True
            self.main_menu_scene.draw()
            self.main_menu_scene.draw_background.assert_called_once()
            self.main_menu_scene.text_plot.draw.assert_called_once()
            self.main_menu_scene.play_button.draw.assert_called_once()


if __name__ == '__main__':
    unittest.main()