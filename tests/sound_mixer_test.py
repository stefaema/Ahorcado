import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from sound_mixer import SoundMixer
import pygame
class TestSoundMixer(unittest.TestCase):

    def test_singleton_instance(self):
        pygame.init()
        mixer1 = SoundMixer()
        mixer2 = SoundMixer()
        self.assertIs(mixer1, mixer2)


if __name__ == '__main__':
    unittest.main()