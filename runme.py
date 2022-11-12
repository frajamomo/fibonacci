from fibonacci import Iterative, Recursive
from fibonacciSequence import FibonacciSequence

if __name__ == '__main__':

    numberOfElements = int(input("Enter number of elements : "))

    algorithm = Iterative()
    fibonacci = FibonacciSequence(algorithm)
    print('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : ', fibonacci.generate(numberOfElements))

    algorithm = Recursive()
    fibonacci = FibonacciSequence(algorithm)
    print('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : ', fibonacci.generate(numberOfElements))