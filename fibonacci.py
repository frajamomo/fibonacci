from abc import ABC, abstractmethod

class Fibonacci(ABC):
    
    @abstractmethod
    def generate(self, numberOfElements: int):
        pass


class Iterative(Fibonacci):

    def generate(self, numberOfElements):
        count = 0
        i,j = 0,1
        retval = []

        if not isinstance(numberOfElements, int):
            raise ValueError("Invalid input")

        while count < numberOfElements:
            retval.append(i)
            temp = i + j
            i = j
            j = temp
            count += 1

        return(retval)


class Recursive(Fibonacci):

    def generate(self, numberOfElements):

        def _fibonacci_req(n):
            if n in {0, 1}:
                return n
            return _fibonacci_req(n-1) + _fibonacci_req(n-2)

        if not isinstance(numberOfElements, int):
            raise ValueError("Invalid input")

        return [_fibonacci_req(n) for n in range(numberOfElements)]