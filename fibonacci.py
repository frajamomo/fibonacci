from abc import ABC, abstractmethod
from functools import lru_cache


class Fibonacci(ABC):

    @abstractmethod
    def generate(self, numberOfElements: int):
        pass


class IterativeWhileLoop(Fibonacci):

    def generate(self, numberOfElements):
        count = 0
        i, j = 0, 1
        retval = []

        if not isinstance(numberOfElements, int):
            raise ValueError("Invalid input")

        while count < numberOfElements:
            retval.append(i)
            temp = i + j
            i = j
            j = temp
            count += 1

        return retval


class IterativeForLoop(Fibonacci):

    def generate(self, numberOfElements):
        i, j = 0, 1
        retval = [0, 1]

        if not isinstance(numberOfElements, int):
            raise ValueError("Invalid input")

        if numberOfElements == 0:
            return []
        if numberOfElements == 1:
            return [0]

        for _ in range(2, numberOfElements):
            temp = i + j
            i = j
            j = temp
            retval.append(temp)

        return retval


class Recursive(Fibonacci):

    def generate(self, numberOfElements):

        @lru_cache()
        def _fibonacci_req(number):
            if number in {0, 1}:
                return number
            return _fibonacci_req(number-1) + _fibonacci_req(number-2)

        if not isinstance(numberOfElements, int):
            raise ValueError("Invalid input")

        return [_fibonacci_req(n) for n in range(numberOfElements)]


class Yield(Fibonacci):

    def _fib(self, num):
        i, j = 0, 1
        for _ in range(num):
            yield i
            i, j = j, i + j

    def generate(self, numberOfElements):
        if not isinstance(numberOfElements, int):
            raise ValueError("Invalid input")

        return list(self._fib(numberOfElements))
