items = [1, 2, 3, 4, 5]

def sqr(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return 0

result = map(sqr, items)

print result

evens = filter(lambda a: a != 0, result)
# function more or less means - if it is false that it is NOT equal to zero print it out
#lambda is just a placeholder...means anonymous function

print evens