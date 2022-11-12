from fibonacci import *

class FibonacciSequence():

    def __init__(self, algorithm):
        self._algorithm = algorithm

    def generate(self, numberOfElements):
        return self._algorithm.generate(numberOfElements)