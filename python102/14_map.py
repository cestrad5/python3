numbers = [1,2,3,4]
n2 = list(map(lambda i : i * 3, numbers))
print (numbers)
print (n2)

zx = [2, 4, 6, 8]
za = [-2, -4, -6]

zz = list(map(lambda i, j : i + j, zx,za))
print (zz)