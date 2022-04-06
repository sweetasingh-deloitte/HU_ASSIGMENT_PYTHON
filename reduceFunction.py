from functools import reduce
def myProd(a, b):
    return a * b

myProd(-1000,500)

numbers = [-1000, 500, -600, 700, 5000, -90000, -17500]

returned_value = reduce(myProd, numbers)
print(returned_value)
