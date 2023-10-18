import unittest
from fibonacci import Iterative_while_loop, Iterative_for_loop, Recursive
from fibonacciSequence import FibonacciSequence

class TestingIterative_while_loop(unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Iterative_while_loop())

    def test_empty_value(self):
        self.assertEqual(self.fibonacci.generate(0), [])

    def test_initial_value(self):
        self.assertEqual(self.fibonacci.generate(1), [0])

    def test_high_value(self):
        self.assertEqual(self.fibonacci.generate(100)[-1], 218922995834555169026)

    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            self.fibonacci.generate("wrong")
        self.assertEqual("Invalid input", str(context.exception))

class TestingIterative_for_loop(unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Iterative_for_loop())

    def test_empty_value(self):
        self.assertEqual(self.fibonacci.generate(0), [])

    def test_initial_value(self):
        self.assertEqual(self.fibonacci.generate(1), [0])

    def test_high_value(self):
        self.assertEqual(self.fibonacci.generate(100)[-1], 218922995834555169026)

    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            self.fibonacci.generate("wrong")
        self.assertEqual("Invalid input", str(context.exception))


class TestingRecursive(unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Recursive())

    def test_empty_value(self):
        self.assertEqual(self.fibonacci.generate(0), [])

    def test_initial_value(self):
        self.assertEqual(self.fibonacci.generate(1), [0])

    def test_high_value(self):
        self.assertEqual(self.fibonacci.generate(20)[-1], 4181 )

    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            self.fibonacci.generate("wrong")
        self.assertEqual("Invalid input", str(context.exception))


if __name__ == '__main__':
    unittest.main()
