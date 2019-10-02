def find_the_largest_sum(lst):
    incl = lst[0]
    excl = 0
    for i in range(1,len(lst)):
        excl_new = max(incl , excl)
        incl = excl + lst[i]
        excl = excl_new
    return max(incl,excl)


print(find_the_largest_sum([5,1,1,5]))



