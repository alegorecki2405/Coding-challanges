def adjacent_product(lst):
    max = min(lst)

    for i in range(0,len(lst)-1):
        if max < lst[i]*lst[i+1]:
            max = lst[i]*lst[i+1]

    return max

print(adjacent_product([3, 6, -2, -5, 7, 3]))