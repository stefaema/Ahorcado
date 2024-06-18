import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import pygame
from unittest.mock import MagicMock, patch


# Importamos las clases
from on_screen_keyboard import KeyOnScreen, KeyboardOnScreen

class TestKeyOnScreen(unittest.TestCase):
    def setUp(self):
        # Mocking the TextToImageTool class and Button class
        with patch.object(KeyOnScreen,'create_image', return_value = MagicMock()), patch.object(KeyOnScreen,'create_button', return_value = MagicMock()):
            mock_image = MagicMock()

            # Create an instance of KeyOnScreen
            self.key = KeyOnScreen(0, 0, 'A', 'mock_font_path', 24, (255, 255, 255), (155, 155, 155), (255, 0, 0), mock_image, 1)

    def test_initial_state(self):
        self.assertFalse(self.key.static)
        self.assertEqual(self.key.get_letter(), 'A')

    def test_draw_initial(self):
        # Mock the Button's draw method to simulate no action
        self.key.button.draw.return_value = False

        mock_surface = MagicMock()
        action = self.key.draw(mock_surface)
        self.assertFalse(action)
        self.assertFalse(self.key.static)

    def test_draw_action(self):
        # Mock the Button's draw method to simulate an action
        self.key.button.draw.return_value = True

        mock_surface = MagicMock()
        action = self.key.draw(mock_surface)
        self.assertTrue(action)
        self.assertTrue(self.key.static)
        
    def test_draw_static(self):
        # Set the key to static and test if draw does not trigger an action
        self.key.static = True
        mock_surface = MagicMock()
        action = self.key.draw(mock_surface)
        self.assertIsNone(action)
        self.assertTrue(self.key.static)


class TestKeyboardOnScreen(unittest.TestCase):
    def setUp(self):
        # Patch the create_key method

        with patch.object(KeyboardOnScreen,'create_key',return_value = MagicMock()):
            # Mock the images returned by TextToImageTool
            mock_image = MagicMock()
            # Create an instance of KeyboardOnScreen
            self.screen = MagicMock()
            
            self.keyboard = KeyboardOnScreen(self.screen, 'mock_font_path', mock_image, 'SECRET', 1)
        
        with patch.object(KeyOnScreen,'create_image', return_value = MagicMock()), patch.object(KeyOnScreen,'create_button', return_value = MagicMock()):
            self.drawable_keyboard = KeyboardOnScreen(self.screen, 'mock_font_path', mock_image, 'SECRET', 1)

    def test_initial_state(self):
        self.assertEqual(len(self.keyboard.keys), 27)  # 27 letters in the Spanish alphabet
        self.assertEqual(self.keyboard.mistakes, 0)
        self.assertEqual("".join(self.keyboard.current_word), "[] [] [] [] [] [] ")

    def test_draw(self):
        # Mock the draw method for each key
        for key in self.keyboard.keys:
            key.draw.return_value = False

        incorrect_action, correct_action = self.keyboard.draw()
        self.assertFalse(incorrect_action)
        self.assertFalse(correct_action)

    # def test_draw_incorrect_key(self):
    #     # Simulate an incorrect key press
    #     incorrect_key = MagicMock()  # Ensure this is a mock object
    #     incorrect_key.draw = MagicMock(return_value=True)  # Mock the draw method

    #     incorrect_action, correct_action = self.drawable_keyboard.draw()
        
    #     # Assert that an incorrect action was registered
    #     self.assertTrue(incorrect_action)
    #     self.assertFalse(correct_action)
        
    #     # Assert that the mistakes count has been incremented
    #     self.assertEqual(self.drawable_keyboard.mistakes, 1)

    # def test_draw_correct_key(self):
    #     # Simulate a correct key press
    #     correct_key = next(key for key in self.keyboard.correct_keys if key.get_letter() == 'S')
    #     correct_key.draw.return_value = True

    #     incorrect_action, correct_action = self.keyboard.draw()
    #     self.assertFalse(incorrect_action)
    #     self.assertTrue(correct_action)
    #     self.assertIn(" S ", self.keyboard.get_current_word())

    # def test_did_win(self):
    #     # Simulate guessing all correct keys
    #     for key in self.keyboard.correct_keys:
    #         if key.get_letter() in 'SECRET':
    #             key.static = True

    #     self.assertTrue(self.keyboard.did_win())

    # def test_did_not_win(self):
    #     # Simulate an incomplete guess of the secret word
    #     for key in self.keyboard.correct_keys:
    #         if key.get_letter() in 'SECRE':
    #             key.static = True

    #     self.assertFalse(self.keyboard.did_win())

    def test_handle_mistakes(self):
        self.keyboard.mistakes = 1
        self.assertTrue(self.keyboard.handle_mistakes())
        self.assertEqual(self.keyboard.mistakes, 0)

    def test_handle_mistakes_no_mistakes(self):
        self.keyboard.mistakes = 0
        self.assertFalse(self.keyboard.handle_mistakes())
        self.assertEqual(self.keyboard.mistakes, 0)

if __name__ == '__main__':
    unittest.main()
