import unittest
from fibonacci import Iterative, Recursive
from fibonacciSequence import FibonacciSequence

class TestingIterative(unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Iterative())

    def test_empty_value(self):
        self.assertEquals(self.fibonacci.generate(0), [])

    def test_initial_value(self):
        self.assertEquals(self.fibonacci.generate(1), [0])

    def test_high_value(self):
        self.assertEquals(self.fibonacci.generate(100)[-1], 218922995834555169026)

    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            self.fibonacci.generate("wrong")
        self.assertEqual("Invalid input", str(context.exception))


class TestingRecursive(unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Recursive())

    def test_empty_value(self):
        self.assertEquals(self.fibonacci.generate(0), [])

    def test_initial_value(self):
        self.assertEquals(self.fibonacci.generate(1), [0])

    def test_high_value(self):
        self.assertEquals(self.fibonacci.generate(20)[-1], 4181 )

    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            self.fibonacci.generate("wrong")
        self.assertEqual("Invalid input", str(context.exception))



if __name__ == '__main__':
    unittest.main()
