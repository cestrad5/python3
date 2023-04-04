import random

def search_number(list, start, end, objective):
    if start > end:
        return False
    
    mid = (end + start)//2
    counter = 1

    if list[mid] == objective:
        return True
    elif list[mid] < objective:
        counter += 1
        return search_number(list, mid +1, end, objective)
    else:
        counter += 1
        return search_number(list, start, mid - 1, objective)
    




if __name__ == '__main__':
    lsize = int(input('Enter the size of your list: '))
    r_start = int(input('Enter the lower bound of the list: '))
    r_end = int(input('Enter the upper bound of the list: '))
    list = [random.randint(r_start, r_end) for i in range(lsize)]
    #print(list)
    list = sorted(list)
    #print(list)
    objective = int(input('Number to lookup?: '))
    #print(objective)
    print(f'The element {objective} {"is in the list" if search_number else "is not in the list"}')
    #print(f'The element was found after {search_number.counter} times')
