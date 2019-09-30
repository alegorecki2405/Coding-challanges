
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

lst = [1,2,3,4,5]
dl = len(lst)

def ile_mozliwosci(dl):
    if dl == 1:
        return 1
    elif dl == 2:
        return 2
    return ile_mozliwosci(dl-1) + ile_mozliwosci(dl-2)

def poprawki(lst,dl):
    ileod = 0
    for i in range(0,dl-1):
        if lst[i]*10 + lst[i+1] > 26:
            ileod+=1
    return ileod





print(ile_mozliwosci(dl)-poprawki(lst,dl))



