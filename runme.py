from fibonacci import IterativeWhileLoop, IterativeForLoop, Recursive, Yield
from fibonacciSequence import FibonacciSequence

if __name__ == '__main__':

    algorithms = [IterativeWhileLoop(),
                  Recursive(),
                  IterativeForLoop(),
                  Yield()]

    numberOfElements = int(input("Enter number of elements : "))

    for algorithm in algorithms:
        fibonacci = FibonacciSequence(algorithm)
        print('{0: <50}'.format('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : '),
              fibonacci.generate(numberOfElements))
