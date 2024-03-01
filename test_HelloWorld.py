# tests/test_HelloWorld.py
import unittest
from HelloWorld import say_hello

class TestHelloWorld(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()

