import random
listsize = int(input('What is the number of items in the list? '))
list = [random.randint(0,20) for i in range(listsize)]

objetive = int(input('Number to lookup? '))


def lookup(list, objetive):
    for i in list:
        if i == objetive:
            r = True
            break
        else:
            r = False
    return r


if lookup(list, objetive) == False:
    print('That number is not at the list')
else:
    print('That number is at the list')

print(list)



