from fibonacci import Iterative_while_loop, Iterative_for_loop, Recursive
from fibonacciSequence import FibonacciSequence

if __name__ == '__main__':

    numberOfElements = int(input("Enter number of elements : "))

    algorithm = Iterative_while_loop()
    fibonacci = FibonacciSequence(algorithm)
    print('{0: <50}'.format('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : '),
          fibonacci.generate(numberOfElements))

    algorithm = Recursive()
    fibonacci = FibonacciSequence(algorithm)
    print('{0: <50}'.format('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : '),
          fibonacci.generate(numberOfElements))

    algorithm = Iterative_for_loop()
    fibonacci = FibonacciSequence(algorithm)
    print('{0: <50}'.format('Fibonacci sequence (' + algorithm.__class__.__name__ + ') : '),
          fibonacci.generate(numberOfElements))
