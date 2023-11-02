from fibonacci import Iterative_while_loop, Iterative_for_loop, Recursive, Yield
from fibonacciSequence import FibonacciSequence

if __name__ == '__main__':

    algorithms = [Iterative_while_loop(),
                  Recursive(),
                  Iterative_for_loop(),
                  Yield()]

    numberOfElements = int(input("Enter number of elements : "))

    for algorithm in algorithms:
        fibonacci = FibonacciSequence(algorithm)
        print('{0: <50}'.format('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : '),
              fibonacci.generate(numberOfElements))
