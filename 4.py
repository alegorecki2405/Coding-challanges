

# Good morning! Here's your coding interview problem for today.
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in
# linear time and constant space. In other words, find the lowest positive
# integer that does not exist in the array. The array can contain
# duplicates and negative numbers as well.

def find_it(lst):
    print(lst)
    lst2 = []
    for i in lst:
        if i>0:
            lst2.append(i)

    x = True
    y = False
    i =1
    while x:
        for j in lst2:
            if i == j:
                y = True
        if y == False:
            return i
        else:
            y = False
            i+=1


print(find_it([3, 4, -1, 1,2,4,5,6,7]))