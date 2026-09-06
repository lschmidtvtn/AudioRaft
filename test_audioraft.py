# test_audioraft.py
"""
Tests for AudioRaft module.
"""

import unittest
from audioraft import AudioRaft

class TestAudioRaft(unittest.TestCase):
    """Test cases for AudioRaft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AudioRaft()
        self.assertIsInstance(instance, AudioRaft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AudioRaft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
