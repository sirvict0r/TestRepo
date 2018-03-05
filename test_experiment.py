import unittest
from Experiment import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        greeter.return_value = 'Hello world!'
        # this test will fail until you change the Greeter to return this expected message
        self.assertEqual(greeter, 'Hello world!')
