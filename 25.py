def sum_two_smallest_nums(lst):
    lst2 = []
    for i in lst:
        if i>=0:
            lst2.append(i)

    x=lst2.pop(lst2.index(min(lst2)))
    y=lst2.pop(lst2.index(min(lst2)))
    return x+y

print(sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]))