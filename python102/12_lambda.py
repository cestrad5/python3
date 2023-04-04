def increment (x):
    x += 1
    #print (x)
    return x

print(increment(10))

incre2 = lambda x: x + 2
print(incre2(20))

suma = lambda x,y: x + y
print(suma(20,10))

full_name = lambda a, b, c: f'Hola {a.title()} {b.title()} {c.title()}'
nombre = full_name("camilo","estrada","botero")
print(nombre)