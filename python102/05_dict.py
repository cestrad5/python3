"""
dict = {}
for i in range(1,6):
    dict[i] = i * 2

print(dict)

dict_v2 = {j: j*3 for j in range(1,6)}
print(dict_v2)

import random

countries = ['col', 'mex', 'us', 'can']
populations = {}
for country in countries:
    populations[country] = random.randint(50,100)

print(populations)

populations_v2 = {country: random.randint(50,100) for country in countries}
print(populations_v2)
"""
name = ['juan', 'ana', 'john']
age = [12,23,34]
dict_v3 = {}
print(list(zip(name,age)))

dict_v3 = {name:age for (name,age) in zip(name,age)}
print(dict_v3)
print("ana age is ", dict_v3['ana'])
