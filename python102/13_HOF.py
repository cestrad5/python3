def increment(x):
    x += 1
    return x

increment_v2 = lambda x: x+1

def hof (x, function):
    return x + function(x)

hof_v2 = lambda x, function: x + function(x)

result = hof(2,increment)
print (result)

result = hof_v2(3,increment)
print (result)
