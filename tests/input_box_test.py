import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import unittest
from unittest.mock import Mock, MagicMock, patch
from input_box import InputBox

class TestInputBox(unittest.TestCase):

    def setUp(self):
        with patch.object(InputBox, 'validate_parameters', return_value = None):
            pygame.init()
            self.image = MagicMock()
            self.input_box = InputBox(self.image, Mock())

    def test_blink_cursor(self): 
        self.input_box.blink_cursor()
        self.assertTrue(self.input_box.blinking_cursor in ["|", ""])

    def test_handle_event_keydown(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a, unicode='a')
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, 'a')

    def test_handle_event_backspace(self):
        self.input_box.text = 'test'
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE)
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, 'tes')

    def test_handle_event_return(self):
        self.input_box.text = 'test'
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.input_box.handle_event(event)
        self.assertNotEqual(self.input_box.text, '', "Return key should not clear text by default")

    def test_verify_text(self):
        self.input_box.text = 'tést'
        result = self.input_box.verify()
        self.assertTrue(result)
        self.assertEqual(self.input_box.text, 'test')

    def test_verify_text_with_invalid_characters(self):
        self.input_box.text = 'test123'
        result = self.input_box.verify()
        self.assertFalse(result)

    def test_verify_text_with_spaces(self):
        self.input_box.text = 'test test'
        result = self.input_box.verify()
        self.assertFalse(result)

    def test_empty_method(self):
        self.input_box.text = 'test'
        self.input_box.empty()
        self.assertEqual(self.input_box.text, '')

    def test_verify_text_empty_string(self):
        self.input_box.text = ''
        result = self.input_box.verify()
        self.assertFalse(result, "Empty string should not pass verification")

    def test_verify_text_only_spaces(self):
        self.input_box.text = '   '
        result = self.input_box.verify()
        self.assertFalse(result, "String with only spaces should not pass verification")

    def test_verify_text_special_characters(self):
        self.input_box.text = '@#$%'
        result = self.input_box.verify()
        self.assertFalse(result, "String with special characters should not pass verification")

    def test_verify_text_numeric(self):
        self.input_box.text = '1234'
        result = self.input_box.verify()
        self.assertFalse(result, "Numeric string should not pass verification")

    def test_verify_text_mixed_characters(self):
        self.input_box.text = 'test123$%'
        result = self.input_box.verify()
        self.assertFalse(result, "String with mixed valid and invalid characters should not pass verification")
    def test_validate_parameters_with_correct_values(self):
        try:
            input_box = InputBox(pygame.Surface((1,1)), (0,0), "asa")
        except ValueError:
            self.fail("validate_parameters() raised ValueError unexpectedly!")

    def test_validate_parameters_with_wrong_image_type(self):
        with self.assertRaises(ValueError):
            input_box = InputBox("pygame.Surface((1,1))", (0,0), "asa")


    def test_validate_parameters_with_wrong_pos_center_type(self):
        with self.assertRaises(ValueError):
            InputBox(pygame.Surface((1,1)), "not a tuple", "self.text")

    def test_validate_parameters_with_wrong_text_type(self):
        with self.assertRaises(ValueError):
            InputBox(pygame.Surface((1,1)), (0,0), 123)    
    
    def test_validate_parameters_with_wrong_verification_strategy_type(self):
        with self.assertRaises(ValueError):
            InputBox(pygame.Surface((1,1)), (0,0), "asa", "not a verification strategy")

if __name__ == '__main__':
    unittest.main()