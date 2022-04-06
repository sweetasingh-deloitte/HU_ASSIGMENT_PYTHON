# define decorator
def multiplication(func):
    def wrapper(num1, num2):
        print("multiplication is :" + str(num1 * num2))
        return func(num1, num2)

    return wrapper


# define the function
@multiplication
def multiply(num1, num2):
    print("multiplication is :" + str(num1 * num2))


# Execute
multiply(10, 2)