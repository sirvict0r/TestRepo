import unittest
from Experiment import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Mock()
        greeteror = Greeter(''Hello world!'')
        greeter.return_value = 'Hello world!'
        # this test will fail until you change the Greeter to return this expected message
        self.assertEqual(greeter, greeteror)
