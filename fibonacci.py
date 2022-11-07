
def fibonacci(numberOfElements):

    count = 0
    i,j = 0,1
    retval = []

    while count < numberOfElements:
        retval.append(i)
        temp = i + j
        i = j
        j = temp
        count += 1

    return(retval)
    

if __name__ == "__main__":
    numberOfElements = int(input("Number of elements of the fibonacci series to be printed:"))
    print(', '.join(str(item) for item in fibonacci(numberOfElements)))