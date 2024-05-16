import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import unittest
from unittest.mock import Mock, MagicMock
from input_box import InputBox

class TestInputBox(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.image = MagicMock()
        self.input_box = InputBox(self.image, Mock())

    def test_blink_cursor(self):
        self.input_box.active = True
        self.input_box.blink_cursor()
        self.assertEqual(self.input_box.blinking_cursor, "|")

    def test_handle_event_active(self):
        event = MagicMock()
        event.type = pygame.MOUSEBUTTONDOWN

        self.input_box.handle_event(event)
        self.assertTrue(self.input_box.active)

    def test_handle_event_inactive(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {})
        self.input_box.handle_event(event)
        self.input_box.handle_event(event)
        self.assertFalse(self.input_box.active)

    def test_handle_event_keydown(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
        event.unicode = 'a'
        self.input_box.active = True
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, 'a')

    def test_handle_event_backspace(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE)
        self.input_box.active = True
        self.input_box.text = 'test'
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, 'tes')

    def test_handle_event_return(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.input_box.active = True
        self.input_box.text = 'test'
        self.input_box.handle_event(event)
        self.assertEqual(self.input_box.text, '')

if __name__ == '__main__':
    unittest.main()