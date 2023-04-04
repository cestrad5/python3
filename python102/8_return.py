def sum_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

result = sum_range(1,101)
print(result)
result_2 = sum_range(result,20221)
print(result_2)