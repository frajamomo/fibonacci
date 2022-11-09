
def fibonacci(numberOfElements):

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

if __name__ == "__main__":
    numberOfElements = int(input("Number of elements of the fibonacci series to be printed: "))
    print(fibonacci(numberOfElements))

