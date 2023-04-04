import functools

numbers = [1,2,3,4]

result = functools.reduce(lambda counter, value: counter + value, numbers)

print (result)
