import unittest
from fibonacci import IterativeWhileLoop, IterativeForLoop, Recursive, Yield
from fibonacciSequence import FibonacciSequence

class AbstractFibonacci(object):

    def test_empty_value(self):
        self.assertEqual(self.fibonacci.generate(0), [])

    def test_initial_value(self):
        self.assertEqual(self.fibonacci.generate(1), [0])

    def test_second_value(self):
        self.assertEqual(self.fibonacci.generate(2), [0, 1])

    def test_high_value(self):
        self.assertEqual(self.fibonacci.generate(100)[-1], 218922995834555169026)
        self.assertEqual(len(self.fibonacci.generate(100)), 100)

    def test_wrong_raises(self):
        with self.assertRaises(ValueError) as context:
            self.fibonacci.generate("wrong")
        self.assertEqual("Invalid input", str(context.exception))


class TestingIterativeWhileLoop(AbstractFibonacci, unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(IterativeWhileLoop())


class TestingIterativeForLoop(AbstractFibonacci, unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(IterativeForLoop())

class TestingRecursive(AbstractFibonacci, unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Recursive())

class TestingYield(AbstractFibonacci, unittest.TestCase):

    def setUp(self):
        self.fibonacci = FibonacciSequence(Yield())


if __name__ == '__main__':
    unittest.main()
