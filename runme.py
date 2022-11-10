
from fibonacci import *


class FibonacciSequence():

    def __init__(self, algorithm):
        self._algorithm = algorithm

    def generate(self, numberOfElements):
        return self._algorithm.generate(numberOfElements)


if __name__ == '__main__':

    algorithm = Iterative()
    fibonacci = FibonacciSequence(algorithm)
    numberOfElements = int(input("Enter number of elements : "))

    print('Fibonacci sequence : ', fibonacci.generate(numberOfElements))