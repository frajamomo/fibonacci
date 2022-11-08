import unittest
from fibonacci import *

class Testing(unittest.TestCase):
    def test_empty_value(self):
        self.assertEquals(fibonacci(0), [])

    def test_initial_value(self):
        self.assertEquals(fibonacci(1), [0])

    def test_high_value(self):
        self.assertEquals(fibonacci(100)[-1], 218922995834555169026)
        
    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            fibonacci("wrong")
        self.assertEqual("Invalid input", str(context.exception))

if __name__ == '__main__':
    unittest.main()