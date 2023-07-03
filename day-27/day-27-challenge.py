# create a function add to add any amount of numbers we pass in to the method
# * tells python that this method will accept variable number of positional arguments
def add(*args):
    # args is a tuple
    res = 0
    for num in args:
        res += num
    return res


print(add(5, 3))
print(add(5, 3, 4))
print(add(4, 3, 3, 7, 3))


# * tells python that this method will accept variable number of keyword arguments
def calculate(n, **kwargs):
    # kwargs is a dictionary
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    print(kwargs["add"], kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
