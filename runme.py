from fibonacci import *

class FibonacciSequence():

    def __init__(self, algorithm):
        self._algorithm = algorithm

    def generate(self, numberOfElements):
        return self._algorithm.generate(numberOfElements)


if __name__ == '__main__':

    numberOfElements = int(input("Enter number of elements : "))

    algorithm = Iterative()
    fibonacci = FibonacciSequence(algorithm)
    print('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : ', fibonacci.generate(numberOfElements))

    algorithm = Recursive()
    fibonacci = FibonacciSequence(algorithm)
    print('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : ', fibonacci.generate(numberOfElements))