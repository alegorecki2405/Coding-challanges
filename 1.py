
#Good morning! Here's your coding interview problem for today.

#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def pierwsza(lst,k):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==k:
                return True
    return False
print(pierwsza([1,2,3,4],7))

